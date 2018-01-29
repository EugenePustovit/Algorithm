#!/bin/python3

import sys


def create_graph_repr(node_count):
    return [[] for l in range(node_count + 1)]


def add_edge(graph, n1, n2):
    graph[n1].append(n2)
    graph[n2].append(n1)

    return graph


def shortest_reach():
    pass

if __name__ == "__main__":
    q = int(input().strip())
    graph_list = []
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        graph = create_graph_repr(n)
        for a1 in range(m):
            u, v = input().strip().split(' ')
            u, v = [int(u), int(v)]
            graph = add_edge(graph, u, v)
        s = int(input().strip())

        graph_list.append([graph, s])

