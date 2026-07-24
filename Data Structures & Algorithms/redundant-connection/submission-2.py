from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        graph = defaultdict(list)

        def has_cycle(src, par):
            vis.add(src)

            for nei in graph[src]:
                if nei not in vis:
                    if has_cycle(nei, src):
                        return True
                elif nei != par:
                    return True

            return False

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            vis = set()
            if has_cycle(u, -1):
                return [u,v]


        return []




        