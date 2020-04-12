from typing import List
from math import -inf


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # D[i] = max subarr sum from 0 to i
        D = [n for n in nums]

        max_sum = D[0]
        for n in range(1, len(nums)):
            if D[n - 1] + nums[n] > nums[n]:
                D[n] = D[n - 1] + nums[n]
            
            if D[n] >= max_sum:
                max_sum = D[n]
                
        return max_sum



        