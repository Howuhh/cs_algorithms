from typing import List
from math import inf


class Solution:
    def rob_rec(self, nums: List[int]) -> int:
        D = [inf] * (len(nums) + 1)
        
        def _max_rob(D, n):
            if n < 0:
                return 0
            if D[n] == inf:
                if 0 <= n <= 1:
                    D[n] = nums[n]
                else:
                    D[n] = max(_max_rob(D, n - 2), _max_rob(D, n - 3)) + nums[n]
            return D[n]

        return max(
            _max_rob(D, len(nums) - 1),
            _max_rob(D, len(nums) - 2),
        )
    
    def rob_iter(self, nums: List[int]) -> int:
        D = [0] + nums
        
        for n in range(3, len(D)):
            D[n] = max(D[n - 2], D[n - 3]) + D[n]
            
        return max(D)