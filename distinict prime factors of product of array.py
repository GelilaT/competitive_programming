class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
            factors = set()
            for num in nums:
                n = 2
                while n * n <= num:
                    while num % n == 0:
                        factors.add(n)
                        num //= n
                    n += 1
                if num > 1:
                    factors.add(num)
            return len(factors)

    
       
