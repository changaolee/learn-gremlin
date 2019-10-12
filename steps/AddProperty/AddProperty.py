#!/usr/bin/env python
#
# @author: braincy
# @time: 2019-10-12
# @reference: [http://tinkerpop-gremlin.cn/#addproperty-step]

import sys

sys.path.append("../../")

from library.graph import Graph
from steps.Common import Common


class AddProperty(object):
    _instances = {}

    @classmethod
    def get_instance(cls, graph_tag='default'):
        if graph_tag not in cls._instances:
            cls._instances[graph_tag] = AddProperty(graph_tag)
        return cls._instances[graph_tag]

    def __init__(self, graph_tag):
        self.g = Graph(graph_tag)
        self.mock_data()

    def mock_data(self):
        # 创建一个 person 类型的顶点
        dsl = """
            g.addV('person')
        """

        ret = self.g.exec_dsl(dsl).result().next()
        print(ret)

    def run(self):
        # 给 person 类型的顶点添加 name 和 age 属性
        dsl = """
            g.V().hasLabel("person").
                property('name', name).
                property('age', age)
        """
        bindings = {
            "name": "stephen",
            "age": "25"
        }

        self.g.exec_dsl(dsl, bindings)
        Common.get_instance().show_graph()


if __name__ == "__main__":
    AddProperty.get_instance().run()
