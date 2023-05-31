class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        arr = [[0 for _ in range(n)]for i in range(m)]
        arr[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if inbound(i, j + 1):
                    arr[i][j] += arr[i][j + 1]
                if inbound(i + 1, j):
                    arr[i][j] += arr[i + 1][j]
        return arr[0][0]