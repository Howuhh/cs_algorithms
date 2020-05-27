from typing import List


class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]

        return self.combinationSum(candidates, k, target)
        
    def combinationSum(self, candidates, k, target):
        combinations = []
        
        def _combine(start_index, comb, tsum):
            if len(comb) == k and tsum == 0:
                combinations.append(comb)
                return
            elif len(comb) > k or tsum < 0:
                return

            for i in range(start_index, len(candidates)):
                num = candidates[i]
                if num > tsum:
                    continue
                _combine(i + 1, comb + [num], tsum - num)
            
        _combine(0, [], target)
        return combinations