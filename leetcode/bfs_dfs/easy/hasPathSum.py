# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.dfs(root, sum)        
    
    def dfs(self, root, target, path_sum=0):
        if not root:
            return False
        if not root.left and not root.right:
            return (path_sum + root.val) == target
        else:
            return (self.dfs(root.left, target, path_sum + root.val) or
                self.dfs(root.right, target, path_sum + root.val))