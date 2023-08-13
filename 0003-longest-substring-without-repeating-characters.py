class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, start, d = 0, 0, {}
        for end, c in enumerate(s):
            if c in d:
                start = max(start, d[c] + 1)
            d[c] = end
            res = max(res, end - start + 1)
        return res


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = 0
#         for i in range(len(s)):
#             tmp = ""
#             for j in range(i, len(s)):
#                 if s[j] not in tmp:
#                     tmp += s[j]
#                 else:
#                     break
#                 res = max(res, len(tmp))
#         return res
