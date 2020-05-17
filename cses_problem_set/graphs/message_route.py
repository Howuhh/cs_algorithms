# https://cses.fi/problemset/task/1667
import sys
# from pprint import pprint
from math import inf
from collections import deque


# TIME LIMIT: too slow for 99999*149997 = 14999550003 (uwu)
# kek, simple BFS have O(n + m), not O(n*m)
def bellman_ford_path(n, edge_list):  # O(n*m)
    distance = [inf] * n
    prev = [None] * n

    distance[0] = 0
    for k in range(n - 1):
        for (f, t, w) in edge_list:
            if distance[f] + w < distance[t]:
                distance[t] = distance[f] + w
                prev[t] = f

    if distance[n - 1] == inf:
        sys.stdout.write("IMPOSSIBLE\n")
        return
    # reconstruct path
    path, end = [str(n)], n - 1
    while end:
        end = prev[end]
        path.append(str(end + 1))

    sys.stdout.write(str(distance[n - 1] + 1) + "\n")
    sys.stdout.write(" ".join(path[::-1]) + "\n")


# Okay, lets try BFS -> much faster!
# LESSON: on unweighted graph bfs best for shortest path
def shortest_bfs_path(adj, n):  # O(n + m)
    visited = [False] * n
    distance = [0] * n
    prev = [None] * n

    queue = deque([0])
    visited[0] = True

    while queue:
        node = queue.pop()

        for neig in adj[node]:
            if visited[neig]:
                continue
            
            visited[neig], distance[neig] = True, distance[node] + 1
            prev[neig] = node
            queue.appendleft(neig)

    if distance[n - 1] == 0:
        sys.stdout.write("IMPOSSIBLE\n")
        return

    path, end = [str(n)], n - 1
    while end:
        end = prev[end]
        path.append(str(end + 1))

    sys.stdout.write(str(distance[n - 1] + 1) + "\n")
    sys.stdout.write(" ".join(path[::-1]) + "\n")
    

def main():
    n, m = map(int, sys.stdin.readline().split())
    # edge_list = []
    adjency = [[] for _ in range(n)]

    for _ in range(m):
        a, b = [int(i) - 1 for i in sys.stdin.readline().split()]
        adjency[a].append(b)
        adjency[b].append(a)
        # edge_list.append([a, b, 1])
        # edge_list.append([b, a, 1])
    
    # print(adjency)
    shortest_bfs_path(adjency, n)
    # bellman_ford_path(n, edge_list)
    # pprint(edge_list)


if __name__ == "__main__":
    main()