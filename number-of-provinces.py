class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def dfs(visited, i):
            if i in visited:
                return 0
            visited.add(i)
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    dfs(visited, j)

            return 1
        
        count = 0
        for i in range(len(isConnected)):
            count += dfs(visited, i)
        
        return count