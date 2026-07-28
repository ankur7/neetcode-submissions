from collections import defaultdict
from collections import deque
class Solution:
    def canFinish(self, n: int, prereq: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegree = [0] * n

        for u , v in prereq:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        finished = []
        while q:
            cur = q.popleft()
            finished.append(cur)
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        print(finished)    
        if len(finished) == n:
            return True
        return False


        


        