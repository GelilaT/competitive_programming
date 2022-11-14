class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix=float("inf")
        count=0
        for j in range(len(nums)):
            count+=nums[j]
            prefix=min(prefix,count)
        if prefix<1:
           return 1-prefix
        return 1