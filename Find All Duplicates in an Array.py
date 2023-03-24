class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ptr = 0
        n = len(nums)
        ans = set()
        while ptr < n:
            idx = nums[ptr] - 1
            if idx != ptr and nums[idx] == nums[ptr]:
                ans.add(nums[ptr])
                ptr += 1
            elif idx != ptr:
                nums[ptr],nums[idx] = nums[idx],nums[ptr]
            else:
                ptr += 1
        return ans
