# https://cses.fi/problemset/task/1672
import sys
import heapq

from pprint import pprint
from math import inf

# time limit! ohh okay, anyway it works but > than 1sek
def floyd_warshall_path(adj_matrix, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])
    return adj_matrix


def dijkstra_shortest_path(adj, n, source, target):
    visited = [False] * n
    distance = [inf] * n

    distance[source] = 0

    heap = [(0, source)]
    heapq.heapify(heap)
    
    while heap:
        weight, node = heapq.heappop(heap)

        if node == target:
            break

        if visited[node] or weight > distance[node]:
            continue
        visited[node] = True

        for neig, w in adj[node]:
            if distance[node] + w < distance[neig]:
                distance[neig] = distance[node] + w

                heapq.heappush(heap, (distance[neig], neig))
    return distance[target]


def main_warshall():
    n, m, q = map(int, input().split())
    adj_matrix = [[inf] * n for _ in range(n)]
    
    for _ in range(m):
        f, t, w = map(int, input().split())
        if w < adj_matrix[f - 1][t -1]: 
            adj_matrix[f - 1][t - 1] = w
            adj_matrix[t - 1][f - 1] = w

    floyd_warshall_path(adj_matrix, n)   

    for _ in range(q):
        f, t = map(int, input().split())

        if f == t:
            adj_matrix[f - 1][t - 1] = 0
        if adj_matrix[f - 1][t - 1] == inf:
            adj_matrix[f - 1][t - 1] = -1
        print(adj_matrix[f - 1][t - 1])


def main():
    n, m, q = map(int, input().split())
    adj = [[] for _ in range(n)]

    for _ in range(m):
        f, t, w = map(int, input().split())
        adj[f - 1].append((t - 1, w))
        adj[t - 1].append((f - 1, w))

    for _ in range(q):
        f, t = map(int, input().split())

        dist = dijkstra_shortest_path(adj, n, f - 1, t - 1)
        print(dist if dist != inf else -1)
    

if __name__ == "__main__":
    main_warshall()