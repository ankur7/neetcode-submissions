"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sweep = [0] * 1000000

        for item in intervals:
            s,e = item.start, item.end
            sweep[s] += 1
            sweep[e] -= 1

        res = 0
        cur = 0
        for item in sweep:
            cur = cur + item
            res = max(res, cur)

        return res