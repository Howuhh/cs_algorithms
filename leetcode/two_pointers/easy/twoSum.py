from typing import List


class Solution:        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        remainder = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in remainder:
                return remainder[diff], i
            remainder[num] = i

    def twoSum_II(self, nums: List[int], target: int) -> List[int]:
        # nums is sorted already, O(1) memory
        start, end = 0, len(nums) - 1
        
        while start <= end:
            two_sum = nums[start] + nums[end]
            if two_sum == target:
                return start + 1, end + 1
            elif two_sum < target:
                start = start + 1
            else:
                end = end - 1
        
