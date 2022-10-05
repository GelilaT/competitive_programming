class Solution(object):
    def maxOperations(self, nums, k):
        counter=0
        nums.sort()
        n=len(nums)
        i=0
        j=n-1
        while i<j:
          if nums[i]+nums[j]==k:
            counter+=1
            i+=1
            j-=1
          elif nums[i]+nums[j]<k:
            i+=1
          else:
            j-=1          
        return counter