from collections import defaultdict


class Solution:
    def frequencySort(self, string: str) -> str:
        if not string:
            return ""
        counts = defaultdict(int)

        for char in string:
            counts[char] += 1
        
        # counting sort of freq
        sorted_counts = self.countSort(counts.items())[::-1]
        
        chars = list(map(lambda tup: tup[0] * tup[1], sorted_counts))
        
        return "".join(chars)
        
    def countSort(self, nums):  # O(n)
        max_freq = max(nums, key=lambda tup: tup[1])[1]
        counts = [0] * (max_freq + 1)
       
        for index, freq in nums:
            counts[freq] = counts[freq] + 1
        
        for i in range(1, len(counts)):
            counts[i] = counts[i] + counts[i - 1]
    
        sorted_arr = [0] * len(nums)
        for index, freq in nums:
            sorted_arr[counts[freq] - 1] = [index, freq]
            counts[freq] = counts[freq] - 1
        
        return sorted_arr