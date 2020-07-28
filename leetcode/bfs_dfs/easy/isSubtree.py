# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s:
            # check is same s and t or left or right
            return (self.isSame(s, t) or 
                    self.isSubtree(s.left, t) or 
                    self.isSubtree(s.right, t))
    
    # check is s and t is the same (just as in p. isSameTree)
    def isSame(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        return (s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right))
        