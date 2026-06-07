"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sweep = defaultdict(int)

        for item in intervals:
            s,e = item.start, item.end
            sweep[s] += 1
            sweep[e] -= 1

        # print(sweep)
        sweep = dict(sorted(sweep.items()))

        res = 0
        cur = 0
        for key, value in sweep.items():
            cur = cur + value
            res = max(res, cur)

        return res