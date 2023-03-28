class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ptr = 0
        ans = []
        while ptr < len(nums):
            idx = nums[ptr] - 1
            if nums[ptr] == nums[idx] and ptr != idx:
                ans.append(nums[ptr])
                break
            if nums[ptr] != nums[idx]:
                nums[ptr], nums[idx] = nums[idx], nums[ptr]
            else:
                ptr += 1
            
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] != i + 1 and nums[i + 1] != i + 1:
                ans.append(i + 1)
                break
        else:
            ans.append(len(nums))
        return ans
