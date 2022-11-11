class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        ans=0
        while i<j:
            if nums[i]<nums[j]:
                area=nums[i]*(j-i)
                ans=max(ans,area)
                i+=1
            else:
                area=nums[j]*(j-i)
                ans=max(ans,area)
                j-=1
        return ans