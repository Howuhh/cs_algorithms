from typing import List

# https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        "Contains Duplicate"
        counts = {}
        for num in nums:
            if num in counts:
                return True
            counts[num] = 1
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        "Contains Duplicate II"
        counts = {}

        for i, num in enumerate(nums):
            if num in counts and abs(i - counts[num]) <= k:
                return True
            counts[num] = i
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], idx_dist: int, val_dist: int) -> bool:
        "Contains Duplicate III"
        if t < 0: return False

        buckets, w = {}, (val_dist + 1)
        for i, num in enumerate(nums):
            b = num // w

            for neigh in (b - 1, b, b + 1):
                if neigh in buckets and abs(num - buckets[neigh]) <= val_dist:
                    return True

            buckets[b] = num
            if i >= idx_dist:
                # num of backets always == idx window
                del buckets[nums[i - idx_dist] // w]
        return False


def test():
    s = Solution()
    assert s.containsNearbyAlmostDuplicate([7, 1, 3], 2, 3) == True
    assert s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3) == False
    assert s.containsNearbyAlmostDuplicate([2, 1], 1, 1) == True
    assert s.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2) == True
    assert s.containsNearbyAlmostDuplicate([7, 2, 8], 2, 1) == True
    assert s.containsNearbyAlmostDuplicate([4, 2], 2, 1) == False


if __name__ == "__main__":
    test()
