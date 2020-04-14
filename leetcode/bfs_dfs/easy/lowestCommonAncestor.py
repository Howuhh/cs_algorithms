# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        root_val, p_val, q_val = root.val, p.val, q.val
        
        if p_val < root_val and q_val < root_val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p_val > root_val and q_val > root_val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root

    def lowestCommonAncestor_iter(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root

        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node

    # faster than 85% but not simple and just my first implementation that works
    def lowestCommonAncestor_naive(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        first_p, first_d = p, self._depth(root, p)
        second_p, second_d = q, self._depth(root, q)
        
        # to common depth
        while first_d != second_d:
            if first_d > second_d:
                first_p, first_d = self._find_parent(root, first_p)
            else:
                second_p, second_d = self._find_parent(root, second_p) 
        
        # until find a common parent
        while first_p != second_p:
            first_p, first_d = self._find_parent(root, first_p)
            second_p, second_d = self._find_parent(root, second_p)
                
        return first_p
        
    def _find_parent(self, root, node, depth=0):
        if node.val < root.val:
            if root.left == node:
                return (root, depth)
            return self._find_parent(root.left, node, depth + 1)
        else:
            if root.right == node:
                return (root, depth)
            return self._find_parent(root.right, node, depth + 1)
        
    def _depth(self, root, node, depth=0):
        if root == node:
            return depth
        elif node.val < root.val:
            return self._depth(root.left, node, depth + 1)
        else:
            return self._depth(root.right, node, depth + 1)