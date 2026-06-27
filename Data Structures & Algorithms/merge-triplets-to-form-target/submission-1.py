class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        mx1 = mx2 = mx3 = 0

        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                mx1 = max(mx1, a)
                mx2 = max(mx2, b)
                mx3 = max(mx3, c)

        return [mx1, mx2, mx3] == target