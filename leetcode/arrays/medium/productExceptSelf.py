from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod_left, prod_right = [1] * n, [1] * n

        for i in range(1, n):
            prod_left[i] = prod_left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            prod_right[i] = prod_right[i + 1] * nums[i + 1]

        return [prod_left[i]*prod_right[i] for i in range(n)]

    def productExceptSelf_constmem(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [1] * n

        for i in range(1, n):
            prod[i] = prod[i - 1] * nums[i - 1]

        acc = 1
        for i in reversed(range(n)):
            prod[i] = prod[i] * acc
            acc = acc * nums[i]

        return prod
