from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        strings = []
        
        def _gen_string(string, left, right):
            if len(string) == 2*n:
                strings.append(string)
                return
            
            if left < n:
                _gen_string(string + "(", left + 1, right)
            
            if left > right:
                _gen_string(string + ")", left, right + 1)
                
        _gen_string("", 0, 0)
        return strings