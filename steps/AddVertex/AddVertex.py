#!/usr/bin/env python
#
# @author: braincy
# @time: 2019-09-27
# @reference: [http://tinkerpop-gremlin.cn/#addvertex-step]

import sys

sys.path.append("../../")

from library.graph import Graph
from steps.Common import Common


class AddVertex(object):
    _instances = {}

    @classmethod
    def get_instance(cls, graph_tag='default'):
        if graph_tag not in cls._instances:
            cls._instances[graph_tag] = AddVertex(graph_tag)
        return cls._instances[graph_tag]

    def __init__(self, graph_tag):
        self.g = Graph(graph_tag)

    def run(self):
        """ 创建一个 person 类型的顶点并设置 id 和 name """
        dsl = "g.addV('person').property(id, uid).property('name', name)"
        bindings = {"name": "stephen", "uid": "1"}

        ret = self.g.exec_dsl(dsl, bindings).result().next()
        print(ret)

        Common.get_instance().show_graph()


if __name__ == "__main__":
    AddVertex.get_instance().run()
