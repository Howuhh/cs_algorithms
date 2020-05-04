from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # for safety check
            before, after = max(0, mid - 1), min(len(nums) - 1, mid + 1)
            
            if nums[before] < nums[mid] > nums[after]:
                return mid
            elif nums[mid] < nums[after]:
                left = mid + 1
            else:
                right = mid - 1
        return mid
        