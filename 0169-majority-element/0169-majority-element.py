class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=0
        for n in nums:
            dic[n]+=1
            if dic[n] > (len(nums)/2):
               return n