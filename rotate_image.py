class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        new=[]
        for i in range(cols):
            for j in range(i,rows):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(rows):
            k=rows-1
            j=0
            while j < k:
                matrix[i][j],matrix[i][k]=matrix[i][k], matrix[i][j]
                j+=1
                k-=1     
        return matrix
