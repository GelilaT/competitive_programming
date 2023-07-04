class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        rows = len(triangle)
        memo = {}

        def minSum(row, col):

            if row == rows - 1:
                memo[(row, col)] = triangle[row][col]
                return triangle[row][col]

            if (row, col) not in memo:
                memo[(row,col)] = min(minSum(row + 1, col), minSum(row + 1, col + 1)) + triangle[row][col]
                
            return memo[(row, col)]
        
        return minSum(0, 0)