class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = [[None] * n for _ in range(n)]

        def helper(row, col):
            if not (0 <= row < n and 0 <= col < n):
                return inf

            if row == n - 1:
                return matrix[row][col]

            if memo[row][col]:
                return memo[row][col]

            res = matrix[row][col] + min(
                helper(row + 1, col - 1), helper(row + 1, col), helper(row + 1, col + 1)
            )
            memo[row][col] = res
            return res

        res = inf
        for col in range(n):
            res = min(res, helper(0, col))
        return res
