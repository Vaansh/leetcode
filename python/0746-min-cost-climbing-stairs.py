class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [None for _ in range(len(cost))]

        def helper(cost, n):
            if n in [0, 1]:
                return cost[n]
            if memo[n]:
                return memo[n]

            memo[n] = cost[n] + min(helper(cost, n - 1), helper(cost, n - 2))
            return memo[n]

        return min(helper(cost, len(cost) - 1), helper(cost, len(cost) - 2))


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         def helper(cost, n):
#             if n in [0, 1]:
#                 return cost[n]
#             return cost[n] + min(helper(cost, n - 1), helper(cost, n - 2))
#         return min(helper(cost, len(cost) - 1), helper(cost, len(cost) - 2))
