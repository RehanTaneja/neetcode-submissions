class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target >= matrix[i][0] and target <= matrix[i][n-1]:
                for j in range(n):
                    if matrix[i][j]==target:
                        return True
                return False
        return False
        