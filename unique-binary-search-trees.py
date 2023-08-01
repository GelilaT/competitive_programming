class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            cur_total = 0
            for j in range(1, i + 1):
                cur_total += dp[i - j] * dp[j - 1]

            dp[i] = cur_total
        
        return dp[-1]