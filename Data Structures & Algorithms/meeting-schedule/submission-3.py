"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)

        for i in range(1, len(intervals)):
            cur_st = intervals[i].start
            prev_end = intervals[i - 1].end

            if cur_st < prev_end:
                return False

        return True
