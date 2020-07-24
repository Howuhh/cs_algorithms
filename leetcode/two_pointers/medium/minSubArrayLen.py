from math import inf
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_len, j = inf, 0
        
        acc = 0
        for i in range(len(nums)):
            acc = acc + nums[i]
            
            while acc >= s:
                min_len = min(min_len, i - j + 1)
                acc = acc - nums[j]
                j = j + 1
                                
        return min_len if min_len != inf else 0