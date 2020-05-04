from typing import List
from math import inf

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        
        curr_min, closest_sum = inf, None
        
        for i in range(0, len(nums)):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                three_sum = nums[left] + nums[i] + nums[right]

                if abs(target - three_sum) < curr_min:
                    curr_min = abs(target - three_sum)
                    closest_sum = three_sum
                
                if nums[left] + nums[i] + nums[right] < target:
                    left = left + 1
                else:
                    right = right - 1
        
        return closest_sum
        