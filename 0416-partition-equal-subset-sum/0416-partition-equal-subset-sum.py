class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        memo = {}
        n = len(nums)
        target = sum(nums) // 2
        def dp(i, cur):
            
            if i >= n or cur >= target:
                return cur == target

            if (i, cur) not in memo:
                memo[(i, cur)] = dp(i + 1, cur + nums[i]) or dp(i + 1, cur)

            return memo[(i, cur)]

        return sum(nums) % 2 == 0 and dp(0, 0)

            

            


        
       
                






            
