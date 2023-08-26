class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return s == "".join([w[0] for w in words])


# class Solution:
#     def isAcronym(self, words: List[str], s: str) -> bool:
#         if len(words) != len(s):
#             return False
#         i = 0
#         for w in words:
#             if w[0] != s[i]:
#                 return False
#             i += 1
#         return True
