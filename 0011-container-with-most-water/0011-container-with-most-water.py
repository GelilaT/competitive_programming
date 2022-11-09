class Solution:
    def maxArea(self, nums: List[int]) -> int:
        ans=0
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]<nums[j]:
                area=nums[i]*(j-i)
                ans=max(ans,area)
                i+=1
            elif nums[j]<=nums[i]:
                area=nums[j]*(j-i)
                ans=max(ans,area)
                j-=1
        return ans                