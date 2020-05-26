from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        
        def _combine(start_index, comb):
            if len(comb) == k:
                combinations.append(comb)
                return
            
            for num in range(start_index, n + 1):
                _combine(num + 1, comb + [num]) 
            
        _combine(1, [])
        
        return combinations