class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        @lru_cache(None)
        def coin(n):
            # nonlocal ans
            nonlocal memo

            if n == 0:
                return 0
            
            ans = inf
            if n in memo:
                return memo[n]
            for c in coins:
                if n >= c:
                    ans = min(ans, coin(n - c) + 1)

            memo[n] = ans
            return ans

        final = coin(amount)
        if final != inf:
            return final
        else:
            return -1