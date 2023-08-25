class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def helper(l, r):
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        res = 0
        for i in range(n):
            res = sum([res, helper(i, i), helper(i, i + 1)])
        return res


# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         def helper(s):
#             return s == s[::-1]

#         return sum(
#             1 for i in range(len(s)) for j in range(i + 1, len(s) + 1) if helper(s[i:j])
#         )
