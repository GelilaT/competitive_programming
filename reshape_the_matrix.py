class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        size=rows*cols
        all_ele=[]
        for row in range(rows):
            for col in range(cols):
                all_ele.append(mat[row][col])
        if r*c != size:
            return mat
        answer=[]
        for row in range(r):
           answer.append(all_ele[row*c:(row*c)+c])
        return answer
