class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0


# class Solution:
#     def divisorGame(self, n: int) -> bool:
#         def helper(n):
#             if n == 2:
#                 return True
#             for x in range(1, n):
#                 if n % x == 0:
#                      if not helper(n - x):
#                          return True
#             return False
#         return helper(n)
