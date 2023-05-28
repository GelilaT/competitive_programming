class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def minCost(n):
            if n < 2:
                return 0
            if n not in memo:
                memo[n] = min(minCost(n - 1) + cost[n - 1], minCost(n - 2) + cost[n - 2])
            return memo[n]
        return minCost(len(cost))