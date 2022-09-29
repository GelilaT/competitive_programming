class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result=[]
        dic={}
        numsorted=sorted(nums)
        for i in range(len(numsorted)):
          if numsorted[i] not in dic:
           dic[numsorted[i]]=i
        for i in nums:
           result.append(dic[i])
        return result
