class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res, l, index = 0, 0, {}
#         for r, r_char in enumerate(s):
#             if r_char in index:
#                 l = max(l, index[r_char] + 1)
#             index[r_char] = r
#             res = max(res, r - l + 1)
#         return res

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