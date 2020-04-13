from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if ord(letters[mid]) <= ord(target):
                left = mid + 1
            else:
                right = mid - 1
                
        return letters[left % len(letters)]
        