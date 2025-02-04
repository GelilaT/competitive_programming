class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        left = 0
        max_sum = cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                left = 0
                cur = 0

            cur += nums[i]
            max_sum = max(max_sum, cur)

        return max_sum
