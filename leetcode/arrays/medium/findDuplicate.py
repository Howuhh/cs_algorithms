from typing import List


# Floyd's Tortoise and Hare algorightm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        "cycle detection -> cycle start == duplicate"
        slow, fast = 0, 0

        # find cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break

        # find cycle start
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
