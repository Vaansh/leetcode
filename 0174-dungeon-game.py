from functools import cache


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        @cache
        def helper(x, y):
            if x == m - 1 and y == n - 1:
                return dungeon[x][y]

            res = max(
                min(0, helper(x + 1, y)) if x + 1 < m else -math.inf,
                min(0, helper(x, y + 1)) if y + 1 < n else -math.inf,
            )

            return res + dungeon[x][y]

        return max(1, 1 - helper(0, 0))
