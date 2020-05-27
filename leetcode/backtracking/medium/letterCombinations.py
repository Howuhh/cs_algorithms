from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        def _combine(start_idx, string):
            if start_idx >= len(digits):
                strings.append(string)
                return

            for char in letters[digits[start_idx]]:
                _combine(start_idx + 1, string + char)
        
        strings = []
        if digits: _combine(0, "")
        
        return strings       