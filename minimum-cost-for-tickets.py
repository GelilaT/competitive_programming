class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [0] * (days[-1] + 1)
        day_s = set(days)

        for i in range(1, days[-1] + 1):
            if i not in day_s:
                dp[i] = dp[i - 1]

            else:
                dp[i] = dp[max(0, i - 1)] + costs[0]
                dp[i] = min(dp[i], dp[max(0, i - 7)] + costs[1])
                dp[i] = min(dp[i], dp[max(0, i - 30)] + costs[2])

        return dp[-1]