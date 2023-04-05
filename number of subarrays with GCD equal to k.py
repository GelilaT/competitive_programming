class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        def GCD(a, b):
            if b == 0:
                return a
            else:
                return GCD(b, a % b)
        for left in range(len(nums)):
            cur = 0
            for right in range(left,len(nums)):
                cur = GCD(cur,nums[right])
                if cur == k:
                    count += 1
        return count

            
            
