class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        i = 0
        result = []

        new_start, new_end = newInterval

        # 1
        while i < n and intervals[i][1] < new_start:
            result.append(intervals[i][:])
            i += 1

        # 2
        while i < n and new_end >= intervals[i][0]:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

        result.append([new_start, new_end])


        #3
        while i < n:
            result.append(intervals[i][:])
            i += 1

        return result