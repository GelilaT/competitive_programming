class Solution(object):
    def targetIndices(self, nums, target):
         numsorted=sorted(nums)
         result=[]
         for i in range(len(numsorted)):
            if target==numsorted[i]:
              result.append(i)
         return result  