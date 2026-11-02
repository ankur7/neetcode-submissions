class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v,t))

        dist = {i + 1: float('inf') for i in range(n)}

        dist[k] = 0

        pq = [(0, k)]

        while pq:
            curr_dist, node = heapq.heappop(pq)

            if curr_dist > dist[node]:
                continue

            for nei, wei in graph[node]:
                new_dist = curr_dist + wei

                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))

        # print(dist)
        result = max(dist.values())

        if result == float('inf'):
            return -1

        return result

            

            


        