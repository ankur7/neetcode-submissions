"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, ints: List[Interval]) -> bool:
        
        n = len(ints)
        if n < 2:
            return True

        ints.sort(key=lambda x: x.start)
        # data.sort(key=lambda x: x[0])

        for i in range(1,n):
            if ints[i].start < ints[i-1].end:
                return False

        return True
