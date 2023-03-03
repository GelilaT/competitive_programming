class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            prev = self.getRow(rowIndex - 1)
            current = [1]

            for i in range(1 , rowIndex):
                current.append(prev[i - 1] + prev[i])
            current.append(1)

            return current 
            
