class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        n = len(prices)
        for i in range(n - 1):
            if prices[i + 1] - prices[i] > 0:
                total += (prices[i + 1] - prices[i])
        return total