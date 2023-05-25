class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        arr = set(nums)
        if len(nums) <= 4:
            return 0

        case1 = nums[-1] - nums[3]
        case2 = nums[-2] - nums[2]
        case3 = nums[-4] - nums[0]
        case4 = nums[-3] - nums[1]

        return min(case1, case2, case3, case4)