from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mask = [0] * len(nums)
        for num in nums:
            mask[num - 1] += num
            
        print(mask)
        return [i + 1 for i, num in enumerate(mask) if (num != 0 and num > i + 1)]