from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def argmax(nums, l, r):
    return max([(nums[i], i) for i in range(l, r)])


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # O(n^2)
        def build_tree(nums, l, r):
            if l == r:
                return None

            max_value, max_idx = argmax(nums, l, r)
            
            root = TreeNode(max_value)
            root.left = build_tree(nums, l, max_idx)
            root.right = build_tree(nums, max_idx + 1, r)
        
            return root

        return build_tree(nums, 0, len(nums))