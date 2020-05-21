from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))

        adj = self.edges_to_adj(prerequisites, numCourses)
        
        visited = [False] * numCourses
        stack = [False] * numCourses
        topsort = deque()

        def _dfs(node, cycle):
            visited[node] = True
            stack[node] = True

            for neig in adj[node]:
                if not visited[neig]:
                    cycle = _dfs(neig, cycle)
                elif stack[neig]:
                    cycle = True

            stack[node] = False
            topsort.append(node)
            return cycle 

        for node in range(numCourses):
            if not visited[node]:
                if _dfs(node, False):
                    return []
                
        return list(topsort)

    def edges_to_adj(self, edges, n):
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
        return adj


