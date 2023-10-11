class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = sorted(set(nums))
        ans = float('inf')
        for i, num in enumerate(nums):
            cur = num + (n - 1)
            idx = bisect_right(nums, cur)

            ans = min(ans, n - (idx - i))

        return ans