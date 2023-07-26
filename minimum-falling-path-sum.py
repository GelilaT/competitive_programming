class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        memo = {}
        rows = cols = len(matrix)
        
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def minSum(row, col):
            
            if not inbound(row, col):
                return inf
            if row == rows - 1:
                return matrix[row][col]

            if (row, col) not in memo:
                memo[(row, col)] = min(minSum(row + 1, col), minSum(row + 1, col + 1), minSum(row + 1, col - 1)) + matrix[row][col]
            return memo[(row, col)]
        
        result = inf
        for i in range(rows):
            result = min(result, minSum(0, i))
        return result