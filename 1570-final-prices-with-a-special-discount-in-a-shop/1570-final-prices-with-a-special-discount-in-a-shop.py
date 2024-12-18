class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        n = len(prices)
        stack = [prices[-1]]
        ans = [price for price in prices]

        for i in range(n - 2, -1, -1):
            while stack and prices[i] < stack[-1]:
                stack.pop()

            if stack:
                ans[i] -= stack[-1]

            stack.append(prices[i])
            
            
        return ans
                


