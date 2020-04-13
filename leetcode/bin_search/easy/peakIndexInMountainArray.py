from typing import List


class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        