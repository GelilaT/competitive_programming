class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       max_sum=-math.inf
       max_aver=0
       for i in range(len(nums)-k+1):
           cur_sum=0
           for j in range(i,i+k):
               cur_sum+=nums[j]
            max_sum=max(cur_sum,max_sum)
        max_aver=max_sum/k
