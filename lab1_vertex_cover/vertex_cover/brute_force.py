from itertools import combinations
from typing import Optional

from vertex_cover.types import VertexSets, EdgeList
from utils.dimacs import edgeList


def brute_force(graph: VertexSets, k: int) -> Optional[set[int]]:
    """
    :param graph: graph represented as vertex sets
    :param k: this many vertices have to cover the graphs
    :return: set of vertices that create the cover if the solution exists,
    otherwise None
    """
    n = len(graph)
    all_combinations = combinations(range(n), k)
    G_edge_list: EdgeList = edgeList(graph)
    list_of_neighbours: list[int][int] = []

    for _ in range(n):
        list_of_neighbours.append([])

    for edge in G_edge_list:
        list_of_neighbours[edge[0] - 1].append(edge[1] - 1)
        list_of_neighbours[edge[1] - 1].append(edge[0] - 1)


    for subgraph in all_combinations:
        covered_edges: set[tuple[int, int]] = set()
        used_vertex_sets: set[int] = set()
        for vertex in subgraph:
            used_vertex_sets.add(vertex)
            edges = list_of_neighbours[vertex - 1]
            for edge in edges:
                u, v = vertex, edge + 1
                if u < v:
                    covered_edges.add((u, v))
                else:
                    covered_edges.add((v, u))

        if covered_edges == set(G_edge_list):
            return used_vertex_sets

    return None
