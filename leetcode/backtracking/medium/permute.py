from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        
        def _permute(perm, chosen):
            if len(perm) == len(nums):
                perms.append(perm)
                return
            
            for i, num in enumerate(nums):
                if chosen[i]:
                    continue
                    
                chosen[i] = True
                _permute(perm + [num], chosen)
                chosen[i] = False
        
        _permute([], [False] * len(nums))
        return perms