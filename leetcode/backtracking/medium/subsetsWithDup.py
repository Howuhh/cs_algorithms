from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n, nums = len(nums), sorted(nums)

        power_set = set()
        for i in range(2**n, 2**(n + 1)):
            mask = bin(i)[3:]
            
            subset = tuple(nums[i] for i in range(n) if mask[i] == "1")
            power_set.add(subset)
            
        return list(power_set)