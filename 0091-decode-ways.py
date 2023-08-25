class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def helper(i):
            if i == n:
                return 1

            if s[i] == "0":
                return 0

            if i in memo:
                return memo[i]

            pair, not_pair = 0, 0
            if i + 2 <= n and int(s[i : i + 2]) <= 26:
                pair = helper(i + 2)
            not_pair = helper(i + 1)

            memo[i] = pair + not_pair
            return memo[i]

        return helper(0)
