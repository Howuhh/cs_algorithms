from typing import List


class Solution:
    # not very efficient, but DP is overkill imho
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        
        def _partition(string, path):
            if not string:
                partitions.append(path)
                
            for i in range(1, len(string) + 1):
                left, right = string[:i], string[i:]
                
                # partition on two parts -> partition right on two and so on -> all partitions of a set
                if self.palindrome(left):
                    _partition(right, path + [left])
        
        _partition(s, [])
        return partitions
        
    def palindrome(self, string):
        return string == string[::-1]
        