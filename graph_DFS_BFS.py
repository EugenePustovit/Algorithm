
import queue

class Graph(object):

    def __init__(self):
        self.vertex = []

    def get_adj(self, v):
        return self.vertex[v]


g = Graph()


def graph_dfs(v):

    visited = []
    visited[v] = True
    adj = v.get_adj(v)

    for n in adj:
        if visited.get(n):
            graph_dfs(n)


def graph_bfs(v, sv):
    queue_v = queue.Queue()
    visited = []
    path = []

    queue_v.put(sv)
    visited[sv] = True

    while queue_v.full():
        vertex = queue_v.get()
        for w in v.get_adj(vertex):
            if not visited.get(w):
                queue_v.put(w)
                visited[w] = True
                path[w] = vertex
