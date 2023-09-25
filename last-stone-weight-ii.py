class Solution:
    def lastStoneWeightII(self, nums: List[int]) -> int:
        
        memo = {}

        def stone(i, total):

            if i == len(nums):
                return total if total >= 0 else float('inf')

            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = min(stone(i + 1, total - nums[i]), stone(i + 1, total + nums[i]))
            return memo[(i, total)]

        return stone(0, 0)