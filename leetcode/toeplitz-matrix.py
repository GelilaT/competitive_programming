class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if i + 1 < row and j + 1 < col:
                    if matrix[i + 1][j + 1] != matrix[i][j]:
                        return False

        return True
