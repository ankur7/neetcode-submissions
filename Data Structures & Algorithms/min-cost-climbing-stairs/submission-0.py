class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        calc_cost = cost[:2]

        for i in range(2, len(cost)):
            # print(i)
            calc_cost.append(min(calc_cost[i-1], calc_cost[i-2]) + cost[i])

        return min(calc_cost[-1], calc_cost[-2])
        