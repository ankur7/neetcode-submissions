class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:


        # valid_triplets = []
        tx, ty, tz = target

        res_x = 0
        res_y = 0
        res_z = 0

        for x,y,z in triplets:
            if x > tx or y > ty or z > tz:
                continue
            res_x = max(res_x, x)
            res_y = max(res_y, y)
            res_z = max(res_z, z)

        return target == [res_x, res_y, res_z]        