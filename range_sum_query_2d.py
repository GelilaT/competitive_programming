class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.matrix=matrix
        self.rows=len(self.matrix)
        self.cols=len(self.matrix[0])
        self.prefix=[[0 for i in range(self.cols+1)] for i in range(self.rows+1)]
        
        for row in range(self.rows):
            for col in range(self.cols):

                self.prefix[row+1][col+1] = self.matrix[row][col] + self.prefix[row+1][col] + self.prefix[row][col+1] - self.prefix[row][col]
        print(self.prefix)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.prefix[row2+1][col2+1] - self.prefix[row2+1][col1] - self.prefix[row1][col2+1] + self.prefix[row1][col1]
        
