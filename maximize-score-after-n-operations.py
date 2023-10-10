class Solution:
    def maxScore(self, nums: List[int]) -> int:

        @cache
        def backtrack(nums):

            ans = 0
            n = len(nums)
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    new = nums[:i] + nums[i + 1: j] + nums[j + 1:]

                    ans = max(ans, n // 2 * gcd(nums[i], nums[j]) + backtrack(new))

            return ans

        return backtrack(tuple(nums))