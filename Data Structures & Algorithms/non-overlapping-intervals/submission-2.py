class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # intervals = [[1,2],[1,4],[2,4],]

        #intervals = [[1,11],[11,22]]

        # intervals=[[1,100],[11,22],[1,11],[2,12]]

        # intervals = [[1, 10], [2, 3], [3, 4]]
        intervals.sort()
        count = 0
        prev_st, prev_end = intervals[0]

        for i in range(1, len(intervals)):
            cur_st, cur_end = intervals[i]

            if cur_st < prev_end:
                count += 1
                prev_end = min(prev_end, cur_end)
            else:
                prev_st, prev_end = cur_st, cur_end

        return count


        