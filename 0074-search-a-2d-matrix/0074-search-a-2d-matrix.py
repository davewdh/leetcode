class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])  # 1, 2
        l, r = 0, rows * cols - 1     # 0, 1
        while l <= r:
            m = (l + r) // 2  # 1
            row, col = m // cols, m % cols # 1 0
            if matrix[row][col] > target: 
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1
            else:
                return True
        return False

