class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}
        def profit(i, buying):
            
            if i >= len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if buying:
                buy = profit(i + 1, not buying) - prices[i]
                jump = profit(i + 1, buying)
                memo[(i, buying)] = max(buy, jump)
            
            else:
                sell = profit(i + 2, not buying) + prices[i]
                jump = profit(i + 1, buying)
                memo[(i, buying)] = max(sell, jump)
            
            return memo[(i, buying)]
        
        return profit(0, True)

