from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return [i for i in range(1, len(nums) + 1) if i not in set(nums)]

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[(nums[i] % n) - 1] += n

        return [i + 1 for i in range(n) if nums[i] <= n]
