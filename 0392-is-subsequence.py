class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        l = 0
        for c in t:
            if c == s[l]:
                l += 1
            if l == len(s):
                return True
        return l == len(s)

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if len(s) == 0:
#             return True

#         stack = [x for x in s[::-1]]
#         for l in t:
#             if l == stack[-1]:
#                 stack.pop()
#             if len(stack) == 0:
#                 return True

#         return len(stack) == 0