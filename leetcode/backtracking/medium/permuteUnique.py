from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms, nums = [], sorted(nums)
        
        def _permute(perm, chosen):
            if len(perm) == len(nums):
                perms.append(perm)
                return
            
            for i, num in enumerate(nums):
                # only use duplicates if prev is used (maintain order)
                if chosen[i] or (i > 0 and num == nums[i - 1] and chosen[i - 1] == False):
                    continue
                
                chosen[i] = True
                _permute(perm + [num], chosen)
                chosen[i] = False
                
        _permute([], [False] * len(nums))
        
        return perms
                
        