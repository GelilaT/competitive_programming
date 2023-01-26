class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
       my_dict={}
       rows=len(matrix)
       cols=len(matrix[0])
       for row in range(rows):
           for col in range(cols):
               diff=col-row
               if diff not in my_dict:
                   my_dict[diff]=matrix[row][col]
               else:
                   if my_dict[diff] != matrix[row][col]:
                       return False
       return True
