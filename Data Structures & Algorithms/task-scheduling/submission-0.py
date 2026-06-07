class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)

        max_heap = []
        for k, v in count.items():
            max_heap.append(-v)

        heapq.heapify(max_heap)

        q = deque()
        time = 0

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap)
                if -cnt - 1 > 0:
                    q.append((cnt + 1, time + n))
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time


        