# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self._merge(t1, t2)
    
    def _merge(self, t1, t2):
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            
            node.left = self._merge(t1.left, t2.left)
            node.right = self._merge(t1.right, t2.right)

            return node
        return t1 or t2