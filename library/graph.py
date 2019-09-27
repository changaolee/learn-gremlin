from gremlin_python.driver import client
from config.graph import vertex_properties, edge_properties
from config.settings import auth_config
import time


class Graph(object):
    instances = {}

    @classmethod
    def instance(cls, graph_tag='default'):
        if graph_tag not in cls.instances:
            cls.instances[graph_tag] = Graph(graph_tag)
        return cls.instances[graph_tag]

    def __init__(self, graph_tag='default'):
        assert graph_tag in auth_config, 'error graph tag'

        config = auth_config[graph_tag]

        self.__client = client.Client(
            url=config['url'],
            traversal_source=config['traversal_source'],
            username=config['username'],
            password=config['password']
        )
        self.vertex_properties = vertex_properties[graph_tag]
        self.edge_properties = edge_properties[graph_tag]

    def save_vertex(self, vertex_type: str, vertex_id: str, properties: dict):
        """
        保存顶点

        :param vertex_type: 顶点类型
        :param vertex_id: 顶点 ID
        :param properties: 顶点属性
        :return: 创建的顶点 vertex
        """
        assert vertex_type in self.vertex_properties, 'vertex type is undefined'
        assert vertex_id, 'vertex id can\'t be empty'

        bindings = {}
        properties_dsl = ""

        # 获取定义的顶点属性及类型
        defined_properties = self.vertex_properties[vertex_type]

        # 校验顶点属性
        for key in properties:
            assert key in defined_properties, 'vertex properties "{}" is undefined'.format(key)
            custom_key = "c_{}".format(key)
            properties_dsl += ".property('{}', {})".format(key, custom_key)
            bindings[custom_key] = defined_properties[key](properties[key])

        add_properties_dsl, update_properties_dsl = self.add_extra_properties(properties_dsl, properties, bindings)

        dsl = "g.inject(c_method).coalesce(g.V(c_vertex_id){}, g.addV(c_vertex_type).property(id, c_vertex_id){})" \
            .format(update_properties_dsl, add_properties_dsl)
        bindings["c_method"] = "save_vertex"
        bindings["c_vertex_id"] = vertex_id
        bindings["c_vertex_type"] = vertex_type

        try:
            callback = self.__client.submitAsync(dsl, bindings)
            result = callback.result().next()
        except Exception as e:
            result = str(e)

        return result

    def save_edge(self, edge_type: str, from_vertex_id: str, to_vertex_id: str, properties: dict, id_extra=""):
        """
        保存边

        :param edge_type: 边类型
        :param from_vertex_id: 边的起始顶点
        :param to_vertex_id: 边的终止顶点
        :param properties: 边属性
        :param id_extra: 构成边 ID 的额外字段
        :return: 创建的边 edge
        """
        assert edge_type in self.edge_properties, 'edge type is undefined'
        assert from_vertex_id and to_vertex_id, 'vertex id can\'t be empty'

        bindings = {}
        properties_dsl = ""

        # 获取定义的顶点属性及类型
        defined_properties = self.edge_properties[edge_type]

        # 校验边属性
        for key in properties:
            assert key in defined_properties, 'edge properties "{}" is undefined'.format(key)
            custom_key = "c_{}".format(key)
            properties_dsl += ".property('{}', {})".format(key, custom_key)
            bindings[custom_key] = defined_properties[key](properties[key])

        add_properties_dsl, update_properties_dsl = self.add_extra_properties(properties_dsl, properties, bindings)

        edge_id = "{}-{}-{}".format(from_vertex_id, to_vertex_id, edge_type)
        if id_extra:
            edge_id += "-{}".format(id_extra)

        dsl = "g.inject(c_method).coalesce(g.E().hasId(c_edge_id){}, V(c_from_vertex_id).addE(c_edge_type)" \
              ".to(V(c_to_vertex_id)).property(id, c_edge_id){})".format(update_properties_dsl, add_properties_dsl)
        bindings["c_method"] = "save_edge"
        bindings["c_edge_id"] = edge_id
        bindings["c_from_vertex_id"] = from_vertex_id
        bindings["c_to_vertex_id"] = to_vertex_id
        bindings["c_edge_type"] = edge_type

        try:
            callback = self.__client.submitAsync(dsl, bindings)
            result = callback.result().next()
        except Exception as e:
            result = str(e)

        return result

    def query_dsl(self, dsl, bindings=None):
        """
        自定义查询语句，模版化参数，最大程度利用服务端 DSL 解析的缓存能力，加速查询的处理过程
        :param dsl: DSL 模板
        :param bindings: DSL 模板参数
        :return: DSL 操作结果
        """
        assert dsl, 'received dsl is None'

        # 屏蔽 drop() 语句
        assert dsl.find('drop') == -1, 'drop operation is forbidden'

        return self.__client.submitAsync(dsl, bindings)

    @classmethod
    def add_extra_properties(cls, properties_dsl, properties, bindings):
        add_properties_dsl, update_properties_dsl = properties_dsl, properties_dsl

        # 默认 is_deleted 被设置为 0
        if "is_deleted" not in properties:
            add_properties_dsl += ".property('is_deleted', c_is_deleted)"
            update_properties_dsl += ".property('is_deleted', c_is_deleted)"
            bindings["c_is_deleted"] = 0

        current_timestamp = int(time.time())

        # 插入操作更新 ctime，utime 默认为 0
        add_properties_dsl += ".property('ctime', c_ctime).property('utime', c_utime_default)"
        bindings["c_ctime"] = current_timestamp
        bindings["c_utime_default"] = 0

        # 更新操作只更新 utime
        update_properties_dsl += ".property('utime', c_utime)"
        bindings["c_utime"] = current_timestamp

        return add_properties_dsl, update_properties_dsl
