class Solution:
    def minSteps(self, x: int) -> int:
        ops = 0
        i = 2
        while i * i <= x:
            while x % i == 0:
                ops += i
                x //= i
            i += 1
        
        if x != 1:
            ops += x
        
        return ops























        # else:
        #     count = 0
        #     while x > 0:
        #         n = 2
        #         while n * 2 <= x:
        #             n *= 2
        #         count += 2
        #         x -= n
        #     return count