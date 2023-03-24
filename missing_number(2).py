class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append("0")
        ptr = 0
        while ptr < n :
            if isinstance(nums[ptr],int):
                idx = nums[ptr]
                if idx != ptr:
                    nums[ptr], nums[idx] = nums[idx], nums[ptr]
                else:
                    ptr += 1
            else:
                ptr += 1
        for i in range(n + 1):
            if nums[i] != i:
                return i
