class Solution(object):
    def numIdenticalPairs(self, nums):
         goodpairs=0
         n=len(nums)
         for i in range(0,n):
            for j in range(i+1,n):
              if nums[i]==nums[j]:
                goodpairs+=1
                j+=1
              else:
                j+=1
            i+=1
         return goodpairs