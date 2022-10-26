class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        maxi=0
        n=len(nums)
        for j in reversed(range((n//2),n)):
            ans=nums[i]+nums[j]
            maxi=max(ans,maxi)
            i+=1
        return maxi