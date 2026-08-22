from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v,w))

        memo = {}

        def dfs(node, edges):
            if node == dst:
                return 0

            if edges == 0:
                return float('inf')

            if (node, edges) in memo:
                return memo[(node, edges)]

            result = float('inf')

            for nei, price in graph[node]:
                result = min(result, price + dfs(nei, edges - 1))

            memo[(node, edges)] = result

            return result

        res = dfs(src, k + 1)

        return -1 if res == float('inf') else res

        # def dfs(src, cost, k):
        #     key = (src, cost, k)
        #     if key in memo:
        #         return memo[key]
        #     nonlocal result
        #     if src == dst:
        #         return cost

        #     if k < 0:
        #         return float('inf')

        #     result = float('inf')
        #     for nei, wt in graph[src]:
        #         result = min(result, dfs(nei, cost + wt, k - 1))
        #     memo[key] = result
        #     return memo[key]

        # result = dfs(src,0,k)
        # if result == float('inf'):
        #     return -1
        # return result



        