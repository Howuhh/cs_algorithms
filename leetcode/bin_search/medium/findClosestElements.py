from typing import List
from heapq import heappush, heappop


class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        heap = []
        [heappush(heap, (abs(num - x), num)) for num in nums]

        k_closest = []
        for i in range(k):
            k_closest.append(heappop(heap)[1])
            
        return sorted(k_closest)
            
    def findClosestElements_BS(self, nums: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(nums) - k
        
        while left < right:
            mid = (left + right) // 2 
            
            if x - nums[mid] > nums[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return nums[left:left+k]
        
    def findClosestElements_TP(self, nums, k, x):  # simple O(n)
        left, right = 0, len(nums) - 1

        while right - left + 1 != k:
            if abs(nums[left] - x) > abs(nums[right] - x):
                left = left + 1
            else:
                right = right - 1

        return nums[left:right+1]
            