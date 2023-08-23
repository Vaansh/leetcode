from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in set(s):
            a, b = s.find(c), s.rfind(c)
            if a < b:
                res += len(set(s[a + 1 : b]))
        return res
