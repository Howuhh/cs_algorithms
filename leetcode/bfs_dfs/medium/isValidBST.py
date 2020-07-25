# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.path = []
        
        self.in_order(root)

        for i in range(len(self.path) - 1):
            if self.path[i] >= self.path[i + 1]:
                return False
            
        return True
    
    def in_order(self, root: TreeNode):
        if root:
            self.in_order(root.left)
            self.path.append(root.val)
            self.in_order(root.right)