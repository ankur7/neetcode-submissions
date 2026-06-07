class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n - 1:
            return False

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()

        def dfs(node, par):
            if node in visit:
                return False

            visit.add(node)
            for nei in graph[node]:
                if nei == par:
                    continue
                res = dfs(nei, node)
                if res == False:
                    return False
            return True

        result = dfs(0,-1) and len(visit) == n
        return result
        