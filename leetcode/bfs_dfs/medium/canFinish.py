from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        adj = self.edges_to_adj(numCourses, prerequisites)

        visited = [False] * numCourses
        recstack = [False] * numCourses
        
        def _dfs(node, cycle):
            visited[node] = True
            recstack[node] = True

            for neig in adj[node]:
                if not visited[neig]:
                    cycle = _dfs(neig, cycle)
                elif recstack[neig]:
                    # back edge
                    cycle = True
            
            recstack[node] = False
            return cycle
        
        for node in range(numCourses):
            if not visited[node]:
                if _dfs(node, False):
                    return False
        return True

        
    def edges_to_adj(self, numCourses, edge_list):
        adj = [[] for _ in range(numCourses)]

        for a, b in edge_list:
            adj[a].append(b)

        return adj

        
    