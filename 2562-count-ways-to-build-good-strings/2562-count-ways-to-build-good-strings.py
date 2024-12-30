class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        memo = {}

        def dp(idx):

            if idx > high:
                return 0

            if idx in memo: return memo[idx]

            ans = 0
            if low <= idx <= high:
                ans = 1

            memo[idx] = ans + dp(idx + zero) + dp(idx + one)
            memo[idx] = memo[idx] % (10 ** 9 + 7)

            return memo[idx]

        return dp(0)
        # print(memo)
        # return ans