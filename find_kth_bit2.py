class Solution:
    def findKthBit(self, n: int, k: int) -> str:
       return str(self.helper(n,k))

    def helper(self,n,k):
        if n == 1:
            return 0
        if k < 2**(n-1):
            return self.helper(n - 1, k)
        elif k == 2**(n-1):
            return 1
        else:
            return 1 - self.helper(n - 1,k - (2*(k - (2 ** (n - 1)))))
        
