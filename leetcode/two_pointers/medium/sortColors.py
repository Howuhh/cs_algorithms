from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1
        
        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red = red + 1
                white = white + 1 
            elif nums[white] == 1:
                white = white + 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue = blue - 1
