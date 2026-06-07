class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not edges:
            return True

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)

        vis = set()

        def dfs(node, par):
            # print(node, par)
            vis.add(node)

            for nei in graph.get(node, []):
                if nei not in vis:
                    if dfs(nei, node) == True:
                        return True
                elif nei != par:
                    return True

            return False

        res = dfs(edges[0][0], None)

        # print(vis)
        if res or len(vis) != n:
            return False
        return True

        
        