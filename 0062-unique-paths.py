# efficient top down
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[None] * n for _ in range(m)]

        def helper(i, j):
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            if memo[i][j]:
                return memo[i][j]

            memo[i][j] = helper(i + 1, j) + helper(i, j + 1)
            return memo[i][j]

        return helper(0, 0)


# top down
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         memo = {}
#         def helper(i, j, visited):
#             if i >= m or j >= n:
#                 return 0
#             if (i, j) in visited:
#                 return 0
#             if i == m - 1 and j == n - 1:
#                 return 1
#             if (i, j) in memo:
#                 return memo[(i, j)]
#             visited.add((i, j))
#             memo[(i,j)] = helper(i + 1, j, visited) + helper(i, j + 1, visited)
#             visited.remove((i, j))
#             return memo[(i,j)]
#         return helper(0, 0, set())

# recursive
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         memo = {}
#         def helper(i, j, visited):
#             if i >= m or j >= n:
#                 return 0
#             if (i, j) in visited:
#                 return 0
#             if i == m - 1 and j == n - 1:
#                 return 1
#             visited.add((i, j))
#             res = helper(i + 1, j, visited) + helper(i, j + 1, visited)
#             visited.remove((i, j))
#             return res
#        return helper(0, 0, set())
