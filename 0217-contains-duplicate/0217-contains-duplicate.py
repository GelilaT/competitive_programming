class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=0
        for n in nums:
            dic[n]+=1
            if dic[n] > 1:
              return True
        return False
           