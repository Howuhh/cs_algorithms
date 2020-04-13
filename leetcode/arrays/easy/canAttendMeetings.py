from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda tup: tup[1])

        prev_end = -1
        for start, end in intervals:
            if start <= prev_end:
                return False
            prev_end = end

        return True


def test():
    s = Solution()
    
    assert s.canAttendMeetings([[0, 8], [9, 10], [12, 14]]) == True
    assert s.canAttendMeetings([[0, 10], [9, 12], [13, 14]]) == False
    assert s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) == False


if __name__ == "__main__":
    test()