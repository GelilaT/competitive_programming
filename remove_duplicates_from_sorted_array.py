class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       i=0
       j=1
       count=1
       while j < len(nums):
           if nums[i] == nums[j]:
               j+=1
           else:
               count+=1
               nums[i+1],nums[j]=nums[j],nums[i+1]
               i+=1
               j+=1
       return count
        
