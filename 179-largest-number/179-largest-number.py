class Solution(object):
  def largestNumber(self, nums):
     for i in nums:
        j=nums.index(i)
        nums[j]=str(i)
     def comparison(num1,num2):
        if num1+num2>num2+num1:
            return -1
        else:
            return 1
     nums=sorted(nums, key=cmp_to_key(comparison))
     return str(int("".join(nums)))