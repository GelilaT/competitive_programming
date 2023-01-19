class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        answer=[[0]*(n-2) for i in range(n-2)]
        for row in range(n-2):
            for col in range(n-2):
                answer[row][col]=max(grid[row_ele][col_ele] for row_ele in range(row,row+3) for col_ele in range(col,col+3))
        return answer
