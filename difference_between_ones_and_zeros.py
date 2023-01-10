class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row=len(grid)
        col=len(grid[0])
        row_dict={}
        for index,val in enumerate(grid):
            ones=0
            for i in range(col):
                if val[i]==1:
                    ones+=1
            row_dict[index]=ones
        
        colmatrix=[[0]*row for x in range(col)]
        col_dict={}
        for i in range(col):
            for j in range(row):
                colmatrix[i][j]+=grid[j][i]

        for index,val in enumerate(colmatrix):
            ones=0
            for i in range(len(val)):
                if val[i]==1:
                    ones+=1
            col_dict[index]=ones
        answer=[[0]*col for x in range(row)]
        for i in range(row):
            for j in range(col):
                answer[i][j]=row_dict[i]+col_dict[j]-(row-col_dict[j])-(col-row_dict[i])
        return answer
