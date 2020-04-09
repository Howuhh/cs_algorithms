from typing import List
# https://leetcode.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        "find missing from 0 to n seq"
        true_sum = (len(nums) * (len(nums) + 1)) / 2
        n_sum = sum(nums)
        
        return true_sum - n_sum