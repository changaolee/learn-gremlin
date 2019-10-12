#!/usr/bin/env python
#
# @author: braincy
# @time: 2019-09-27
# @reference: [http://tinkerpop-gremlin.cn/#addedge-step]

import sys

sys.path.append("../../")

from library.graph import Graph
from steps.Common import Common


class AddEdge(object):
    _instances = {}

    @classmethod
    def get_instance(cls, graph_tag='default'):
        if graph_tag not in cls._instances:
            cls._instances[graph_tag] = AddEdge(graph_tag)
        return cls._instances[graph_tag]

    def __init__(self, graph_tag):
        self.g = Graph(graph_tag)
        self.mock_data()

    def mock_data(self):
        # 创建两个 person 类型的顶点并设置 id 和 name
        dsl = """
            g.addV('person').
                property(id, uid_1).
                property('name', name_1).
              addV('person').
                property(id, uid_2).
                property('name', name_2)
        """
        bindings = {
            "uid_1": "1", "name_1": "marko",
            "uid_2": "2", "name_2": "stephen"
        }

        ret = self.g.exec_dsl(dsl, bindings).result().next()
        print(ret)

    def run(self):
        # 给两个 person 顶点添加 knows 类型的边
        dsl = """
            g.V(from_uid).addE('knows').to(V(to_uid)).
                property(id, edge_id)
        """
        bindings = {
            "from_uid": "1",
            "to_uid": "2",
            "edge_id": "1-knows-2"
        }

        ret = self.g.exec_dsl(dsl, bindings).result().next()
        print(ret)

        Common.get_instance().show_graph()


if __name__ == "__main__":
    AddEdge.get_instance().run()
