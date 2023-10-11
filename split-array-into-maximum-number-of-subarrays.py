class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        mini = nums[0]
        for i in range(1, len(nums)):
            mini &= nums[i]

        if mini != 0:
            return 1

        else:
            res = nums[0]
            count = 0
            for i in range(len(nums)):
                res &= nums[i]
                if res == 0:
                    count += 1
                    res = nums[i + 1] if i != len(nums) - 1 else 0

            return count