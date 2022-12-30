class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        maxnum=max(2,n)
        if n==1:
            return 2
        for i in range(1,(2*n)+1):
            if i%2==0 and i%n==0:
                return i
                break
