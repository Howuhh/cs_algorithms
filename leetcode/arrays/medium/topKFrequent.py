from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        # counting sort of freq
        sorted_counts = self.countSort(counts.items())
        return sorted_counts[-k:]
        
    def countSort(self, nums):  # O(n)
        max_freq = max(nums, key=lambda tup: tup[1])[1]
        counts = [0] * (max_freq + 1)
       
        for index, freq in nums:
            counts[freq] = counts[freq] + 1
        
        for i in range(1, len(counts)):
            counts[i] = counts[i] + counts[i - 1]
    
        sorted_arr = [0] * len(nums)
        for index, freq in nums:
            sorted_arr[counts[freq] - 1] = index
            counts[freq] = counts[freq] - 1
        
        return sorted_arr
