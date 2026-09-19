from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.dct = defaultdict(int)       
        

    def add(self, point: List[int]) -> None:
        self.dct[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        cur_x, cur_y = point
        
        res = 0
        for k,v in list(self.dct.items()):
            d_x, d_y = k

            if d_x == cur_x or d_y == cur_y:
                continue

            if abs(cur_x - d_x) != abs(cur_y - d_y):
                continue

            p1_x, p1_y = cur_x, d_y
            p2_x, p2_y = d_x, cur_y

            if (p1_x, p1_y) in self.dct and (p2_x, p2_y) in self.dct:
                res += v * self.dct[(p1_x, p1_y)] * self.dct[(p2_x, p2_y)]
            
        return res
        
