class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsum=[0]
        for i in range(len(nums)):
            prefixsum.append(prefixsum[i]+nums[i])
        for i in range(len(nums)):
            if prefixsum[i]==prefixsum[-1]-prefixsum[i]-nums[i]:
                return i
        return -1