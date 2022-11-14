class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        i=0
        sums=sum(arr[:k])

        average=sums/k
        if average>=threshold:
           count+=1
        for j in range(k,len(arr)):
            sums=sums-arr[i]+arr[j]
            average=sums/k
            if average>=threshold:
              count+=1
            i+=1
        return count  