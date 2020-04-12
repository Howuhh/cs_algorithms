from bisect import bisect_left
from typing import List


class Solution:
    def sortedSquares_sort(self, nums: List[int]) -> List[int]:
        return list(sorted(map(lambda x: x**2, nums)))

    def sortedSquares_merge(self, nums: List[int]) -> List[int]:
        # O(n)
        last_neg = bisect_left(nums, 0)

        merged = []
        
        i, j = last_neg - 1, last_neg
        while i >= 0 and j < len(nums):
            if nums[i]**2 < nums[j]**2:
                merged.append(nums[i]**2)
                i = i - 1
            else:
                merged.append(nums[j]**2)
                j = j + 1
        
        while i >= 0:
            merged.append(nums[i]**2)
            i -= 1
        
        while j < len(nums):
            merged.append(nums[j]**2)
            j += 1
                
        return merged

    def sortedSquares_pointers(self, nums: List[int]) -> List[int]:
        nums = [n**2 for n in nums]

        squared = []
        neg, pos = 0, len(nums) - 1

        while neg <= pos:
            if nums[neg] >= nums[pos]:
                squared.append(nums[neg])
                neg = neg + 1
            else:
                squared.append(nums[pos])
                pos = pos - 1

        return squared[::-1]
        