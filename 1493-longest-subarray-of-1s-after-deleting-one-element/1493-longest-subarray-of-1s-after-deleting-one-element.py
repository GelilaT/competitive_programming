class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i=j=0
        ans=0
        k=1
        for j in range(len(nums)):
              if nums[j]==0:
                    k-=1
              while i<len(nums) and k<0:
                        if nums[i]==0:
                            k+=1
                        i+=1
              ans=max(ans,j-i)
        return ans