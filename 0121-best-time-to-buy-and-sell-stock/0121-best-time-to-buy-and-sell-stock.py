class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        i=0
        j=1
        ans=0
        while j<len(nums):
            if nums[i]<nums[j]:
                profit=nums[j]-nums[i]
                ans=max(ans,profit)
            else:
                i=j
            j+=1
        return ans