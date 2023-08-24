class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def uniquePathsWithObstacleHelper(i, j):
            if i == m - 1 and j == n - 1:
                return 1 if obstacleGrid[i][j] == 0 else 0

            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = uniquePathsWithObstacleHelper(
                i + 1, j
            ) + uniquePathsWithObstacleHelper(i, j + 1)
            return memo[(i, j)]

        return uniquePathsWithObstacleHelper(0, 0)


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         memo = [[None] * n for _ in range(m)]
#         def helper(i, j):
#             if i >= m or j >= n:
#                 return 0
#             if obstacleGrid[i][j] == 1:
#                 memo[i][j] = 0
#                 return memo[i][j]
#             if i == m - 1 and j == n - 1:
#                 return 1
#             if memo[i][j]:
#                 return memo[i][j]
#             memo[i][j] = helper(i + 1, j) + helper(i, j + 1)
#             return memo[i][j]
#         return helper(0, 0)
