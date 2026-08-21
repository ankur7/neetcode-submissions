import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        # 5 4 3 2 1
        # 5 4 3


        max_heap = []

        for x,y in points:
            cur_dis = (x**2 + y**2)**(1/2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-1 * cur_dis, x, y))
            elif len(max_heap) == k:
                max_val = -1 * max_heap[0][0]
                if cur_dis < max_val:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-1 * cur_dis, x, y))

        # print(max_heap)
        result = []
        for dist, x, y in max_heap:
            result.append([x,y])
        return result



        