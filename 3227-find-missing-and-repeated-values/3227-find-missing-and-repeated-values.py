class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        arr = [0] * (n * n)
        for i in range(n):
            for j in range(n):
                arr[grid[i][j] - 1] += 1

        ans = [0, 0]
        for i in range(len(arr)):
            if arr[i] == 2:
                ans[0] = i + 1

            elif arr[i] == 0:
                ans[1] = i + 1

        return ans


        