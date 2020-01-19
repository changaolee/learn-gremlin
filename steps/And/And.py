#!/usr/bin/env python
#
# @author: braincy
# @time: 2019-10-12
# @reference: [http://tinkerpop-gremlin.cn/#and-step]

import sys

sys.path.append("../../")

from library.graph import Graph
from steps.Common import Common


class And(object):
    _instances = {}

    @classmethod
    def get_instance(cls, graph_tag='default'):
        if graph_tag not in cls._instances:
            cls._instances[graph_tag] = And(graph_tag)
        return cls._instances[graph_tag]

    def __init__(self, graph_tag):
        self.g = Graph(graph_tag)
        self.mock_data()

    def mock_data(self):
        # 创建两个 person 类型的顶点
        dsl = """
            g.addV('person').
                property(id, uid_1).
                property('age', age_1).
              addV('person').
                property(id, uid_2).
                property('age', age_2)
        """
        bindings = {
            "uid_1": 1, "age_1": 20,
            "uid_2": 2, "age_2": 25
        }

        ret = self.g.exec_dsl(dsl, bindings).result().next()
        print(ret)

    def run(self):
        dsl = """
            g.V().has('age', inside(start_1, end_1)).
                and().
                has('age', outside(start_2, end_2)).
            values('age')
        """
        # (10, 30) 与 (-∞, 15) U (20, +∞) 的交集 => 25
        bindings = {'start_1': 10, 'end_1': 30, 'start_2': 15, 'end_2': 20}

        vertex_list = self.g.exec_dsl(dsl, bindings).result().next()
        print("ans: {}".format(vertex_list))

        Common.get_instance().show_graph()


if __name__ == "__main__":
    And.get_instance().run()
