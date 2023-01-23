class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
       rows=len(matrix)
       cols=len(matrix[0])
       zerorow=[]
       zerocol=[]
       default=[0]*cols
       for i in range(rows):
           for j in range(cols):
               if matrix[i][j] == 0:
                   zerorow.append(i)
                   zerocol.append(j)
       for i in range(len(zerorow)):
            matrix[zerorow[i]]=default
       for i in range(len(zerocol)):
            for j in range(rows):
                matrix[j][zerocol[i]]=0
       return matrix
