from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.dfs(root)

    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        # draw for [1, 2] case -> max for root
        if root.left and root.right:
            return min(self.dfs(root.left), self.dfs(root.right)) + 1
        else:
            return max(self.dfs(root.left), self.dfs(root.right)) + 1

    def bfs(self, root: TreeNode) -> int:
        queue = deque([(root, 1)] if root else [])
        
        while queue:
            node, depth = queue.pop()
            
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.appendleft((node.left, depth + 1))
            if node.right:
                queue.appendleft((node.right, depth + 1))
        return 0