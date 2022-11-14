class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsum=[]
        postfixsum=[0]*len(nums)
        prefix=0
        postfix=0
        for i in range(len(nums)):
           prefix+=nums[i]
           prefixsum.append(prefix)
        for i in range(len(nums)-1,-1,-1):
            postfix+=nums[i]
            postfixsum[i]+=postfix
        for i in range(len(nums)):
            if prefixsum[i]==postfixsum[i]:
                return i
        return -1