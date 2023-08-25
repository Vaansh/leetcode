class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        mod = 10**9 + 7

        @cache
        def helper(i, j, moves):
            if not (0 <= i < m and 0 <= j < n):
                return 1

            if moves == maxMove:
                return 0

            return (
                helper(i + 1, j, moves + 1)
                + helper(i - 1, j, moves + 1)
                + helper(i, j + 1, moves + 1)
                + helper(i, j - 1, moves + 1)
            )

        return helper(startRow, startColumn, 0) % mod


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        mod = 10**9 + 7
        memo = {}

        def helper(i, j, moves):
            if not (0 <= i < m and 0 <= j < n):
                return 1

            if moves == maxMove:
                return 0

            if (i, j, moves) in memo:
                return memo[(i, j, moves)] % mod

            memo[(i, j, moves + 1)] = (
                helper(i + 1, j, moves + 1)
                + helper(i - 1, j, moves + 1)
                + helper(i, j + 1, moves + 1)
                + helper(i, j - 1, moves + 1)
            )
            return memo[(i, j, moves + 1)] % mod

        return helper(startRow, startColumn, 0) % mod
