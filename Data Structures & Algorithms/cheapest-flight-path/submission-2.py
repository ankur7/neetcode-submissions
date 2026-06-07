from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for s, d, p in flights:
            graph[s].append((d, p))
        
        result = float('inf')

        def dfs(node, stops, cur_price):
            nonlocal result
            
            # prune if already worse
            if cur_price >= result:
                return
            
            # if too many stops
            if stops > k + 1:
                return

            # reached destination
            if node == dst:
                result = cur_price
                return

            for nei, price in graph[node]:
                dfs(nei, stops + 1, cur_price + price)

        dfs(src, 0, 0)
        return -1 if result == float('inf') else result
