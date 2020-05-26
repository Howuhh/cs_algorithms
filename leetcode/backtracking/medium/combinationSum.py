from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        def _combine(start_index, comb, t_sum):
            if start_index >= len(candidates):
                return 
            
            if t_sum <= 0:
                if t_sum == 0:
                    combinations.append(comb)
                return
            
            for i in range(start_index, len(candidates)):
                num = candidates[i]
                
                if num > t_sum:
                    continue
                # all combinations with j num
                _combine(i, comb + [num], t_sum - num)
                
        _combine(0, [], target)

        return combinations