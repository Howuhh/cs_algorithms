from typing import List
from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # main idea: remove all leaves layer by layer until 1 or 2 nodes a left -> nodes with max height
        if not edges:
            return [0]
        adj = self.edges_to_adj(edges, n)    
        deg = [len(adj[i]) for i in range(n)]
        
        queue = deque([node for node in range(n) if deg[node] <= 1])
        
        while n > 2:
            n -= len(queue)
        
            level_queue = deque()
            # remove one layer
            while queue:
                node = queue.pop()

                for neig in adj[node]:
                    deg[neig] -= 1
                    if deg[neig] == 1:
                        level_queue.appendleft(neig)
            queue = level_queue
        
        return list(queue)
        
    def edges_to_adj(self, edges, n):
        adj = [[] for _ in range(n)]
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        return adj
        