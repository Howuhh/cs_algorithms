from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        count, left = 0, 0

        acc = 1
        for right in range(len(nums)):
            acc = acc * nums[right]

            while acc >= k:
                acc = acc / nums[left]
                left = left + 1
            
            count += right - left + 1
        return count