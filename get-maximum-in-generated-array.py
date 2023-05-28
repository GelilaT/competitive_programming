class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        ans = [0, 1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                ans.append(ans[i // 2])
            else:
                ans.append(ans[i // 2] + ans[i // 2 + 1])
        return max(ans)