#!/usr/bin/env python
#
# @author: braincy
# @time: 2019-09-29
# @reference: [http://tinkerpop-gremlin.cn/#aggregate-step]

import sys

sys.path.append("../../")

from library.graph import Graph
from steps.Common import Common


class Aggregate(object):
    _instances = {}

    @classmethod
    def get_instance(cls, graph_tag='default'):
        if graph_tag not in cls._instances:
            cls._instances[graph_tag] = Aggregate(graph_tag)
        return cls._instances[graph_tag]

    def __init__(self, graph_tag):
        self.g = Graph(graph_tag)
        self.mock_data()

    def mock_data(self):
        # 创建两个 person 类型的顶点和两个 song 类型的顶点
        dsl = """
            g.addV('person').
                property(id, uid_1).
                property('name', name_1).
              addV('person').
                property(id, uid_2).
                property('name', name_2).
              addV('song').
                property(id, song_id_1).
                property('name', song_name_1).
              addV('song').
                property(id, song_id_2).
                property('name', song_name_2)
        """
        bindings = {
            "uid_1": "u1", "name_1": "marko",
            "uid_2": "u2", "name_2": "stephen",
            "song_id_1": "s1", "song_name_1": "song-A",
            "song_id_2": "s2", "song_name_2": "song-B"
        }

        ret = self.g.exec_dsl(dsl, bindings).result().next()
        print(ret)

        # 添加三条边： marko-like->song-A；stephen-like-song-A；stephen-like-song-B
        dsl = """
            g.V(uid_1).addE('like').to(V(song_id_1)).
              V(uid_2).addE('like').to(V(song_id_1)).
              V(uid_2).addE('like').to(V(song_id_2))
        """

        ret = self.g.exec_dsl(dsl, bindings).result().next()
        print(ret)

    def run(self):
        # 找到与 marko 有共同兴趣的人还喜欢哪些 marko 还没喜欢的 歌曲
        dsl = """
            g.V(uid_1).out('like').aggregate('x').
                in('like').out('like').
                where(without('x')).
                values('name')
        """
        bindings = {
            "uid_1": "u1"
        }

        self.g.exec_dsl(dsl, bindings)
        Common.get_instance().show_graph()


if __name__ == "__main__":
    Aggregate.get_instance().run()
