import heapq

from typing import List
from random import randint


class Solution:
    def findKthLargest_partial_sort(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        last = None
        for i in range(k):
            last = -heapq.heappop(heap)
            
        return last
            
    def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            rand_pivot = randint(left, right)
            nums[left], nums[rand_pivot] = nums[rand_pivot], nums[left]
            
            pivot = self.partition(nums, left, right)
            
            if pivot == len(nums) - k:
                return nums[pivot]
            elif pivot < len(nums) - k:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1
    
    def partition(self, nums, left, right):
        x, pivot = nums[left], left
        
        for i in range(left + 1, right + 1):
            if nums[i] < x:
                pivot = pivot + 1
                nums[i], nums[pivot] = nums[pivot], nums[i]
        
        nums[left], nums[pivot] = nums[pivot], nums[left]
        
        return pivot