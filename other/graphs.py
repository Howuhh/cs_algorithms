import pysnooper
import heapq

from collections import deque
from math import inf
from pprint import pprint
from copy import deepcopy


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


# not very efficient, just for examples 
def adjency_to_matrix(adj, weights=False):
    adj_matrix = [[inf] * len(adj) for _ in range(len(adj))]

    for i in range(len(adj)):
        for j in range(len(adj)):
            if i == j:
                adj_matrix[i][j] = 0

    for i in range(len(adj)):
        for neig in adj[i]:
            if weights:
                neig, w = neig
            else:
                neig, w = neig, 1
            adj_matrix[i][neig] = w

    return adj_matrix


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


# Shortest paths
def bellman_ford_path(nodes, edges, source):  # O(V*E)
    distance = [inf] * len(nodes)
    distance[source] = 0

    for _ in range(len(nodes) - 1):
        for (f, t, w) in edges:
            distance[t] = min(distance[t], distance[f] + w)

    return distance


def dijkstra_path(adj, source):  # O(V + E*log(E))
    distance = [inf] * len(adj)
    visited = [False] * len(adj)
    prev = [None] * len(adj)

    distance[source] = 0
    
    heap = [(0, source)]
    heapq.heapify(heap)

    while heap:
        weight, node = heapq.heappop(heap)

        # check for duplicate
        if visited[node] or weight > distance[node]:
            continue
        visited[node] = True

        # update path for all neigbors
        for neig, neig_w in adj[node]:
            if distance[node] + neig_w < distance[neig]:
                distance[neig] = distance[node] + neig_w
                prev[neig] = node

                heapq.heappush(heap, (distance[neig], neig))

    return distance, prev


# reconstruct shortest path from source to target: [source, ..path.., target]
def dijkstra_path_find(adj, source, target):
    dist, prev = dijkstra_path(adj, source)
    path = []

    if dist[target] == inf:
        return path

    path.append(target)

    while target:
        target = prev[target]
        path.append(target)
    
    return path[::-1]


# shortest path between all pairs
def floyd_warshall_path_simple(adj_matrix):  # O(V^3)
    dist, n = deepcopy(adj_matrix), len(adj_matrix)

    # shortes paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist


# shortest path between all pairs
def floyd_warshall_path(adj_matrix):  # O(V^3)
    dist, n = deepcopy(adj_matrix), len(adj_matrix)
    next_ = [[None] * n for _ in range(n)]

    # setup next for path reconstruction
    for i in range(n):
        for j in range(n):
            if dist[i][j] != inf:
                next_[i][j] = j

    # shortes paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_[i][j] = next_[i][k]
                # dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist, next_


def floyd_warshall_find(adj_matrix, start, end):
    dist, next_ = floyd_warshall_path(adj_matrix)
    path = []

    if dist[start][end] == inf:
        return path

    path.append(start)
    while start != end:
        start = next_[start][end]
        path.append(start)

    return path


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def Union(self, a, b):
        parent_a, parent_b = self.Find(a), self.Find(b)
    
        # smaller to bigger
        if self.size[parent_a] < self.size[parent_b]:
            parent_a, parent_b = parent_b, parent_a

        # b -> a (or a -> b)
        self.parent[parent_b] = parent_a

        self.size[parent_a] += self.size[parent_b]
        self.size[parent_b] = 0

    def Find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.Find(self.parent[a])

        return self.parent[a]

    def Same(self, a, b):
        return self.Find(a) == self.Find(b)


# Minimum spanning tree of the graph
def kruskals_mst(nodes, edge_list):
    union = UnionFind(len(nodes))
    sorted_edges = sorted(edge_list, key=lambda tup: tup[2])

    mst = []
    for (a, b, w) in sorted_edges:
        if not union.Same(a, b):
            union.Union(a, b)            
            mst.append([a, b, w])

    return mst


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
    graph_adj = [
        [(1, 2), (3, 7), (2, 3)],
        [(0, 2), (3, 3), (4, 5)],
        [(0, 3), (3, 2)],
        [(2, 2), (0, 7), (1, 3)],
        [(1, 5), (3, 2)]
    ]


    # pprint(
    #     floyd_warshall_find(
    #         adjency_to_matrix(graph_adj, weights=True), 0, 2
    #     )
    # )
    # pprint(dijkstra_path_find(graph_adj, 0, 2))

    # graph_edges = adjency_to_edge_list(graph_adj, weights=True)
    # graph_nodes = list(range(len(graph_adj)))

    kruskals_test = [
        [0, 1, 10],
        [0, 2, 6],
        [0, 3, 5],
        [1, 3, 15],
        [2, 3, 4]
    ]
    assert kruskals_mst(list(range(4)), kruskals_test) == [[2, 3, 4], [0, 3, 5], [0, 1, 10]]

    # print(bellman_ford_path(graph_nodes, graph_edges, 0))
    # print(dijkstra_path_find(graph_adj, 0, 4))

    # edges = [
    #     [0, 1, -1],
    #     [0, 2, 4],
    #     [1, 2, 3],  
    #     [1, 3, 2],  
    #     [1, 4, 2],  
    #     [3, 2, 5],  
    #     [3, 1, 1], 
    #     [4, 3, -3]
    # ]
    # nodes = [i for i in range(5)]

    # assert bellman_ford_path(nodes, edges, 0) == [0, -1, 2, -2, 1]


if __name__ == "__main__":
    test_paths()