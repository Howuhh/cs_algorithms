from collections import deque
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.bfs(root)
        
    def bfs(self, root: TreeNode) -> List[List[int]]:
        queue = deque([root] if root else [])
        stack = []
        
        while queue:
            level_nodes = []
            while queue:
                level_nodes.append(queue.pop())
                
            stack.append([node.val for node in level_nodes])
            
            for node in level_nodes:
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
        return stack