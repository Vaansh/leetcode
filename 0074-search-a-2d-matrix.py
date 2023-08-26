class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []
        for r in range(len(matrix)):
            if matrix[r][0] <= target <= matrix[r][-1]:
                row.append(r)

        if len(row) == 0:
            return False

        for r in row:
            if target in matrix[r]:
                return True

        return False
