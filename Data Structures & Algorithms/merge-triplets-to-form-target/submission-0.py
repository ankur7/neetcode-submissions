class Solution:
    def mergeTriplets(self, triplets, target):
        valid = []

        # Step 1: keep only valid triplets
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                valid.append((a, b, c))

        # Step 2: merge using max
        res = [0, 0, 0]
        for a, b, c in valid:
            res[0] = max(res[0], a)
            res[1] = max(res[1], b)
            res[2] = max(res[2], c)

        # Step 3: compare with target
        return res == target
        