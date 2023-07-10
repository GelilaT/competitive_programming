class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:
        n = len(q)
        memo = {}
        def solve(i):

            if i >= n:
                return 0

            if i not in memo:
                memo[i] = max(solve(i + 1 + q[i][1]) + q[i][0], solve(i + 1))
            return memo[i]
        
        return solve(0)