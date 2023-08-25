class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(s):
            return s == s[::-1]

        return sum(
            1 for i in range(len(s)) for j in range(i + 1, len(s) + 1) if helper(s[i:j])
        )
