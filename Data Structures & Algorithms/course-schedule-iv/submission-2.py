class Solution:
    def checkIfPrerequisite(self, numCourses: int, pre_req: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for s, d in pre_req:
            graph[s].append(d)

        memo = {}  # (node, tgt) -> bool

        def dfs(node, tgt):
            if (node, tgt) in memo:
                return memo[(node, tgt)]

            if node == tgt:
                memo[(node, tgt)] = True
                return True

            for nei in graph[node]:
                if dfs(nei, tgt):
                    memo[(node, tgt)] = True
                    return True

            memo[(node, tgt)] = False
            return False

        return [dfs(u, v) for u, v in queries]