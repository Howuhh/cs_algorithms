from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums))*2 - sum(nums)

    # TODO: bit XOR solution
    def singleNumber_xor(self, nums: List[int]) -> int:
        acc = 0
        for num in nums:
            acc ^= num

        return acc

    def singleNumber_two(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2