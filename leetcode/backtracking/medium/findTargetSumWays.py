from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def _countWays(start, cumsum, cache):
            if (start, cumsum) not in cache:
                if start == len(nums):
                    cache[(start, cumsum)] = 1 if cumsum == target else 0
                else:
                    left = _countWays(start + 1, cumsum + nums[start], cache)
                    right = _countWays(start + 1, cumsum - nums[start], cache)
                    
                    cache[(start, cumsum)] = left + right
            return cache[(start, cumsum)]

        return _countWays(0, 0, {})