class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        p = n // 2
        mod = 10 ** 9 + 7
        
        odd = pow(5, ceil(n / 2), mod)
        even = pow(4, n // 2, mod)

        return odd * even % mod