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

    def subsets_rec(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        
        def gen_sub(start_index, curr_set):
            power_set.append(curr_set)
            
            for k in range(start_index, len(nums)):
                gen_sub(k + 1, curr_set + [nums[k]])
                
        gen_sub(0, [])
        return power_set

    def subsets_bits(self, nums: List[int]) -> List[List[int]]:
        bitmasks = []
        power_set = []
        
        def gen_masks(curr_mask=""):
            if len(curr_mask) == len(nums):
                bitmasks.append(curr_mask)
                return
                
            gen_masks(curr_mask + "0")
            gen_masks(curr_mask + '1')
        
        gen_masks()
        for mask in bitmasks:
            power_set.append([nums[i] for i in range(len(nums)) if mask[i] == "1"])
            
        return power_set