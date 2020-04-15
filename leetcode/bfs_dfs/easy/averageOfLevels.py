from collections import deque
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mean(array):
    return sum(array) / len(array)


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        return self.bfs(root)
        
    def bfs(self, root: TreeNode) -> List[float]:
        averages = []
        queue = deque([root] if root else [])
        
        while queue:
            level_nodes = []
            while queue:
                level_nodes.append(queue.pop())
            
            # compute level average
            averages.append(mean([node.val for node in level_nodes]))
            
            for node in level_nodes:
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
    
        return averages
        