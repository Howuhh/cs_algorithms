import pysnooper

from collections import deque
from math import inf


def dfs(adj, node):
    visited = [False] * len(adj)
    path = []

    def _dfs(node):
        if visited[node]:
            return
        visited[node] = True
        
        path.append(node)

        for neig in adj[node]:
            _dfs(neig)

    _dfs(node)

    return path


def bfs(adj, root):
    visited = [False] * len(adj)
    distance = [0] * len(adj)
    
    queue = deque([root])
    visited[root] = True

    while queue:
        node = queue.pop()

        for neig in adj[node]:
            if visited[neig]:
                continue
            
            visited[neig] = True
            distance[neig] = distance[node] + 1
            queue.appendleft(neig)

    return distance


def graph_components(adj):
    components = [None] * len(adj)
    visited = [False] * len(adj)

    # dfs to label components & visited
    def _dfs(node, comp):
        if visited[node]:
            return

        visited[node] = True
        components[node] = comp
        for neig in adj[node]:
            _dfs(neig, comp)

    # dfs for each not visited node
    start_comp = -1
    for node in range(len(adj)):
        if visited[node]:
            continue

        start_comp = start_comp + 1
        _dfs(node, start_comp)

    return components


@pysnooper.snoop("graph.txt")
def bellman_ford_path(nodes, edges, source):
    distance = [inf] * len(nodes)
    distance[source] = 0

    for i in range(len(nodes) - 1):
        for (f, t, w) in edges:
            distance[t] = min(distance[t], distance[f] + w)

    return distance


def adjency_to_edge_list(adj, weights=False):
    edge_list = []

    for node, neigs in enumerate(adj):
        for neig in neigs:
            if weights:
                edge = [node, neig[0], neig[1]]
            else:
                edge = [node, neig]
            edge_list.append(edge)

    return edge_list


def test_traversal():
    test_graph = [None] * 8

    test_graph[0] = [1, 3]
    test_graph[1] = [2, 4]
    test_graph[2] = [1, 4]
    test_graph[3] = [0]
    test_graph[4] = [1, 2]
    test_graph[5] = [6]
    test_graph[6] = []
    test_graph[7] = [] 

    print(dfs(test_graph, 0))
    # print(graph_components(test_graph))


def test_paths():
    # graph_adj = [
    #     [(1, 2), (3, 7), (2, 3)],
    #     [(0, 2), (3, 3), (4, 5)],
    #     [(0, 3), (3, -2)],
    #     [(2, -2), (0, 7), (1, 3)],
    #     [(1, 5), (3, 2)]
    # ]
    # graph_edges = adjency_to_edge_list(graph_adj, weights=True)
    # graph_nodes = list(range(len(graph_adj)))

    edges = [
        [0, 1, -1],
        [0, 2, 4],
        [1, 2, 3],  
        [1, 3, 2],  
        [1, 4, 2],  
        [3, 2, 5],  
        [3, 1, 1], 
        [4, 3, -3]
    ]
    nodes = [i for i in range(5)]

    assert bellman_ford_path(nodes, edges, 0) == [0, -1, 2, -2, 1]


if __name__ == "__main__":
    test_paths()