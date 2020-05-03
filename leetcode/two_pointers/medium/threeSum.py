from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]
        sums, nums = set(), sorted(nums)
        
        for a in range(0, len(nums)):
            # search for a + b = -c
            left, right, target = a + 1, len(nums) - 1, -nums[a]
            
            while left < right:                
                if nums[left] + nums[right] == target:
                    sums.add((nums[a], nums[left], nums[right]))
                    right = right - 1
                    left = left + 1
                elif nums[left] + nums[right] < target:
                    left = left + 1
                else:
                    right = right - 1
        return sums

    def threeSum_naive(self, nums: :
        nums, three_sum = sorted(nums), set()
        
        for a in range(0, len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    if nums[a] + nums[b] + nums[c] == 0:
                        three_sum.add((nums[a], nums[b], nums[c]))
        return three_sum
