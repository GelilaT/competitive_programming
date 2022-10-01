class Solution(object):
    def sortColors(self,nums):
        count=[0,0,0]
        for i in range(len(nums)):
            if nums[i]==0:
                count[0]+=1
            elif nums[i]==1:
                count[1]+=1
            else:
                count[2]+=1
        for j in range(count[0]):
            nums[j]=0
        for j in range(count[0],count[1]+count[0]):
            nums[j]=1
        for j in range(count[1]+count[0],count[0]+count[2]+count[1]):
            nums[j]=2
        return nums
