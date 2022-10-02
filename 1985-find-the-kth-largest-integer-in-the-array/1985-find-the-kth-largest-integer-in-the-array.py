class Solution(object):
    def kthLargestNumber(self, nums, k):
         converted=[]
         for l in nums:
            converted.append(int(l))
         converted.sort() 
         converted.reverse()   
         return str(converted[k-1])
