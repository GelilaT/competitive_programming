class Solution:
    def coloredCells(self, n: int) -> int:
        
        def recur(n):
            if n == 1:
                return 1

            return recur(n - 1) + (4 * (n - 1))

        return recur(n)