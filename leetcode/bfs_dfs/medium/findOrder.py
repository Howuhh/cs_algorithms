from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))

        adj, _ = self.edges_to_adj(prerequisites, numCourses)
        
        visited = [0] * numCourses
        topsort = deque()

        def _dfs(node, cycle):
            visited[node] = 1

            for neig in adj[node]:
                if visited[neig] == 0:
                    cycle = _dfs(neig, cycle)
                elif visited[neig] == 1:
                    cycle = True

            visited[node] = 2
            topsort.append(node)
            return cycle 

        for node in range(numCourses):
            if not visited[node]:
                if _dfs(node, False):
                    return []
                
        return list(topsort)

    def edges_to_adj(self, edges, n):
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for a, b in edges:
            adj[a].append(b)
            indegree[b] += 1

        return adj, indegree

    def findOrderInDegree(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj, indegree = self.edges_to_adj(prerequisites, numCourses)

        queue = deque([node for node in range(numCourses) if indegree[node] == 0])
        topsort = deque()

        while queue:
            node = queue.pop()
            topsort.appendleft(node) # nodes with 0 indegree

            for neig in adj[node]:
                indegree[neig] -= 1
                
                if indegree[neig] == 0:
                    queue.appendleft(neig)
        
        return list(topsort) if len(topsort) == numCourses else []


if __name__ == "__main__":
    s = Solution()
    test = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    n = 6

    print(s.findOrderInDegree(numCourses=n, prerequisites=test))