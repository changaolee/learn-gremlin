#!/usr/bin/env python
#
# @author: braincy
# @time: 2019-09-27

from library.graph import Graph
import json


class Common(object):
    _instances = {}

    @classmethod
    def get_instance(cls, graph_tag='default'):
        if graph_tag not in cls._instances:
            cls._instances[graph_tag] = Common(graph_tag)
        return cls._instances[graph_tag]

    def __init__(self, graph_tag):
        self.g = Graph(graph_tag)

    def show_graph(self):
        vertex_list = self._get_vertex()
        edge_list = self._get_edge()

        data = {}
        if vertex_list:
            data["vertex"] = vertex_list
        if edge_list:
            data["edge"] = edge_list

        print(json.dumps(data, indent=4, sort_keys=True))
        print("-" * 50)

    def _get_vertex(self):
        dsl = "g.V().valueMap(true)"
        callback = self.g.exec_dsl(dsl)

        result = []
        for ret in callback.result():
            data = self._format_graph_fields(ret)
            result.append(data)

        return result

    def _get_edge(self):
        dsl = "g.E().valueMap(true)"
        callback = self.g.exec_dsl(dsl)

        result = []
        for ret in callback.result():
            data = self._format_graph_fields(ret)
            result.append(data)

        return result

    @staticmethod
    def _format_graph_fields(graph_data):
        format_data = {}
        for k, v in graph_data.items():
            format_data[str(k)] = v[0] if type(v) == list else v

        format_data['id'] = format_data['T.id']
        format_data['label'] = format_data['T.label']

        del format_data['T.id']
        del format_data['T.label']

        return format_data
