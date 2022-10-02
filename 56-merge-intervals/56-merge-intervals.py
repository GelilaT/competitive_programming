class Solution(object):
    def merge(self, intervals):
         intervals.sort(key=lambda i:i[0])
         result=[intervals[0]]
         for i in intervals[1:]:
            last=result[-1][1]
            if i[0]<=last:
              result[-1][1]=max(last,i[1])
            else:
              result.append([i[0],i[1]])
         return result