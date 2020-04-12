from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        # sum(i, j) = sum[j] - sum[i - 1]
        self.cum_nums = self.accumulate(nums)
        
    def accumulate(self, nums):
        cum_sum = [0] * (len(nums) + 1)
        for n in range(len(nums)):
            cum_sum[n + 1] = nums[n] + cum_sum[n]
        return cum_sum
        
    def sumRange(self, i: int, j: int) -> int:
        return self.cum_nums[j + 1] - self.cum_nums[i]
        