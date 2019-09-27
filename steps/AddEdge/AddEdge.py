#!/usr/bin/env python
#
# @author: braincy
# @time: 2019-09-27 15:41
# @reference: [http://tinkerpop-gremlin.cn/#addedge-step]

import sys

sys.path.append("../../")

from library.graph import Graph


class AddEdge(object):
    _instances = {}

    @classmethod
    def get_instance(cls, graph_tag='default'):
        if graph_tag not in cls._instances:
            cls._instances[graph_tag] = AddEdge(graph_tag)
        return cls._instances[graph_tag]

    def __init__(self, graph_tag):
        self.g = Graph(graph_tag)
