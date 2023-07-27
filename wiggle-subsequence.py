class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # if len(nums) <= 2:
        #     return len(nums)
        
        big = small = 1
        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                big = small + 1

            if nums[i] < nums[i - 1]:
                small = big + 1
        
        return max(small, big)