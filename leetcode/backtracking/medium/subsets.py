from typing import List


class Solution:
    def subsets_iter(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]
        
        for num in nums:
            new_sets = []
            for sub in power_set:
                new_sets.append(sub + [num])
            power_set.extend(new_sets)
        return power_set