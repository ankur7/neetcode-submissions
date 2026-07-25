from collections import defaultdict
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:

        res = []

        queue = []

        indegree = [0] * n
        graph = defaultdict(list)

        for u , v in prerequisites:
            indegree[v] += 1
            graph[u].append(v)

        for ind in range(n):
            if indegree[ind] == 0:
                queue.append(ind)

        print(1, indegree)
        print(2, queue)

        while queue:
            cur = queue.pop(0)
            res.append(cur)
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        if len(res) == n:
            return res[::-1]
        return []
        