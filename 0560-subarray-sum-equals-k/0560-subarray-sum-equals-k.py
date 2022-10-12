class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       result=0
       cursum=0
       prefixsums={0:1}
       for i in nums:
            cursum+=i
            diff=cursum-k
            result+=prefixsums.get(diff,0)
            prefixsums[cursum]=1+prefixsums.get(cursum,0) 
       return result