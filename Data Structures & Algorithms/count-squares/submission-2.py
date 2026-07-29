from collections import defaultdict

"""
     p1      xdyd

     xy      p2

0.0
"""

class CountSquares:

    # [1,1] [2,2] [1,2] [2,1]

    def __init__(self):
        self.point_count = defaultdict(int)  

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1        

    def count(self, point: List[int]) -> int:

        res = 0

        x,y = point

        for k, v in self.point_count.items():
            xd,yd = k

            if (xd == x or yd == y or abs(xd - x) != abs(yd - y)):
                continue

            p1 = (x, yd)
            p2 = (xd, y)

            res += (v * self.point_count.get(p1, 0) * self.point_count.get(p2, 0))

        return res       
        
