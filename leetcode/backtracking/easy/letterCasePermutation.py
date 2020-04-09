from typing import List


class Solution:
    def letterCasePermutation_TopDown(self, S: str) -> List[str]:
        char_arr = list(S)
        cache = set()

        def _CasePermutation(S, idx):
            if idx == -1:
                string = "".join(S)
                if string in cache:
                    return []
                return [string]
            
            S_low = S.copy()
            S_low[idx] = S_low[idx].lower()
            
            S_upp = S.copy()
            S_upp[idx] = S_upp[idx].upper()
            return _CasePermutation(S_low, idx - 1) + _CasePermutation(S_upp, idx - 1)
        
        return _CasePermutation(char_arr, len(char_arr) - 1)

    def letterCasePermutation_BotUp(self, S: str) -> List[str]:
        result = []
        
        def _CasePermutation(char_arr, S, idx, acc):
            if idx == len(char_arr):
                acc.append(S)
                return
            
            if char_arr[idx].isalpha():
                _CasePermutation(char_arr, S + char_arr[idx].upper(), idx + 1, acc)
                _CasePermutation(char_arr, S + char_arr[idx].lower(), idx + 1, acc)
            else:    
                _CasePermutation(char_arr, S + char_arr[idx], idx + 1, acc)
        
        _CasePermutation(S, "", 0, result)
        return result
        