class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(isWater)
        n = len(isWater[0])
        queue = deque()

        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n

        ans = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append([i, j])
                    ans[i][j] = 0

        while queue:
            i, j = queue.popleft()
            for row_change, col_change in directions:
                x = i + row_change
                y = j + col_change
                if not inbound(x, y) or ans[x][y] != -1:
                    continue

                if ans[x][y] == -1:
                    ans[x][y] = ans[i][j] + 1

                queue.append([x, y])

        return ans


