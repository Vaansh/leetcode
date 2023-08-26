class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[None] * n for _ in range(m)]

        def helper(grid, i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j]

            if i >= m or j >= n:
                return inf

            if memo[i][j]:
                c = memo[i][j]
            else:
                memo[i][j] = grid[i][j] + min(
                    helper(grid, i + 1, j), helper(grid, i, j + 1)
                )
            return memo[i][j]

        return helper(grid, 0, 0)
