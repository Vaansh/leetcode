class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, grid = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                elif val in row[r] or val in col[c] or val in grid[r // 3, c // 3]:
                    return False
                row[r].add(val)
                col[c].add(val)
                grid[r // 3, c // 3].add(val)
        return True

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         def get_cols(matrix):
#             res = [[] for _ in range(9)]
#             for i, row in enumerate(matrix):
#                 for j, r in enumerate(row):
#                     res[j].append(r)
#             return res

#         def valid_row_or_col(val):
#             seen = []
#             for c in val:
#                 if c == ".":
#                     continue
#                 if c in seen:
#                     return False
#                 seen.append(c)
#             return True

#         def valid_grid(grid):
#             seen = []
#             for row in grid:
#                 for r in row:
#                     if r == ".":
#                         continue
#                     if r in seen:
#                         return False
#                     seen.append(r)
#             return True

#         for r in board:
#             if not valid_row_or_col(r):
#                 return False

#         for c in get_cols(board):
#             if not valid_row_or_col(c):
#                 return False

#         for i in range(0, 9, 3):
#             for j in range(0, 9, 3):
#                 grid = [row[j : j + 3] for row in board[i : i + 3]]
#                 if not valid_grid(grid):
#                     return False

#         return True
