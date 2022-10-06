class Solution(object):
    def topKFrequent(self, nums, k):
     from collections import Counter
     nums.sort()
     count=Counter(nums)
     result=[]
     s=sorted(count, key=count.get, reverse=True)
     for i in range(k):
          result.append(s[i])
     return result            