from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations, candidates = [], sorted(candidates)
        
        def _combine(start_index, comb, tsum):
            if start_index > len(candidates):
                return
            
            if tsum <= 0:
                if tsum == 0:
                    combinations.append(comb)
                return
            
            for i in range(start_index, len(candidates)):
                num = candidates[i]
                # skip duplicates 
                if num > tsum or (i > start_index and num == candidates[i - 1]):
                    continue
                    
                _combine(i + 1, comb + [num], tsum - num)
                
        _combine(0, [], target)
        return combinations
        