from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
       
        last_good = last
        
        for pos in reversed(range(last)):
            if pos + nums[pos] >= last_good:
                last_good = pos
            
        return last_good == 0
            