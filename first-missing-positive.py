class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # ptr = 0
        n = len(nums)
        for i in range(n):
            while nums[i] != i + 1 and 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = nums[i] , nums[nums[i] - 1]
            i += 1
        print(nums)
        for idx,val in enumerate(nums):
            if idx != val - 1:
                return idx + 1
        return n + 1