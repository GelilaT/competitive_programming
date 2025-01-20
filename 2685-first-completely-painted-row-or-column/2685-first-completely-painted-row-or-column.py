class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        n = len(mat[0])
        m = len(mat)

        rows = [0] * m
        cols = [0] * n

        rowVal = [0] * (m * n + 1)
        colVal = [0] * (m * n + 1)

        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                rowVal[num] = i
                colVal[num] = j
        
        for i, val in enumerate(arr):
            rows[rowVal[val]] += 1
            cols[colVal[val]] += 1

            if rows[rowVal[val]] == n or cols[colVal[val]] == m:
                return i



        