# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.depth(root)[0]

    def depth(self, root):
        if root:
            left_diameter, left_depth = self.depth(root.left)
            right_diameter, right_depth = self.depth(root.right)
            
            diameter = max(left_diameter, right_diameter, left_depth + right_depth)
            depth = max(left_depth, right_depth) + 1

            return (diameter, depth)
        # (diameter, depth)
        return (0, 0)