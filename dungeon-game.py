class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        rows, cols = len(dungeon), len(dungeon[0])
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        if dungeon[-1][-1] >= 0:
            dp[-1][-1] = 1
        else:
            dp[-1][-1] = abs(dungeon[-1][-1]) + 1

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                
                if i == rows - 1 and j == cols - 1:
                    continue

                if dungeon[i][j] < 0:
                    if inbound(i + 1, j) and inbound(i, j + 1):
                        dp[i][j] = abs(dungeon[i][j]) + min(dp[i + 1][j], dp[i][j + 1])
                    
                    elif inbound(i + 1, j):
                        dp[i][j] = abs(dungeon[i][j]) + dp[i + 1][j]
                    
                    elif inbound(i, j + 1):
                        dp[i][j] = abs(dungeon[i][j]) + dp[i][j + 1]

                else:
                    if inbound(i + 1, j) and inbound(i, j + 1):
                        if min(dp[i + 1][j], dp[i][j + 1]) <= dungeon[i][j]:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]

                    elif inbound(i + 1, j):
                        if dp[i + 1][j] <= dungeon[i][j]:
                            dp[i][j] = 1
                        
                        else:
                            dp[i][j] = dp[i + 1][j] - dungeon[i][j]

                    elif inbound(i, j + 1):
                        if dp[i][j + 1] <= dungeon[i][j]:
                            dp[i][j] = 1
                        
                        else:
                            dp[i][j] = dp[i][j + 1] - dungeon[i][j]        

        return dp[0][0]