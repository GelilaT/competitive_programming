class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp1 = [0] * (n + 3)
        dp2 = [0] * (n + 3)
        if n == 1:
            return nums[0]
            
        for i in range(n - 1, 0, -1):
            dp1[i] = max(dp1[i + 2], dp1[i + 3]) + nums[i]

        for i in range(n - 2, -1, -1):
            dp2[i] = max(dp2[i + 2], dp2[i + 3]) + nums[i]

        max1 = max(dp1[1], dp1[2])
        max2 = max(dp2[0], dp2[1])

        return max(max1, max2)