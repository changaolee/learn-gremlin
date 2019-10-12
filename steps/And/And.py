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
        pass

    def run(self):
        dsl = ""
        bindings = {}

        self.g.exec_dsl(dsl, bindings)
        Common.get_instance().show_graph()


if __name__ == "__main__":
    And.get_instance().run()
