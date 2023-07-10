class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}
        def Sum(n):

            if n < 0:
                return 0

            if n == 0:
                return 1
            
            if n in memo:
                return memo[n]

            result = 0
            for num in nums:
                result += Sum(n - num)
            memo[n] = result

            return memo[n]
        
        return Sum(target)