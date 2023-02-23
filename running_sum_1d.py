class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running=0
        running_sum=[]
        for i in range(len(nums)):
            running+=nums[i]
            running_sum.append(running)
        return running_sum
