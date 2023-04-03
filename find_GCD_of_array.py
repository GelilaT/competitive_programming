class Solution:
    def findGCD(self, nums: List[int]) -> int:
        first = min(nums)
        second = max(nums)
        def GCD(a, b):
            if b == 0:
                return a
            return GCD(b, a % b)
        return GCD(first, second)
            
