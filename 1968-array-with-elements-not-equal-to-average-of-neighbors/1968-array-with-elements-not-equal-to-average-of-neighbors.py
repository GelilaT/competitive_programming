class Solution(object):
    def rearrangeArray(self, nums):
         nums.sort()
         result=[]
         right=len(nums)-1
         left=0
         while len(result)!=len(nums):
           result.append(nums[left])
           left+=1
           if left<=right:
            result.append(nums[right])
            right-=1
         return result