class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def helper(x, y):
            if not (0 <= x < m and 0 <= y < n):
                return 0

            if obstacleGrid[x][y] == 1:
                return 0

            if x == m - 1 and y == n - 1:
                return 0 if obstacleGrid[x][y] == 1 else 1

            if (x, y) in memo:
                return memo[(x, y)]

            res = helper(x + 1, y) + helper(x, y + 1)
            memo[(x, y)] = res
            return res

        return helper(0, 0)


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
