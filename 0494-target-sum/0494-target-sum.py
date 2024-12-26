class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        result = 0
        def findTarget(index, n):

            nonlocal result
            
            if index == len(nums):
                if n == target: 
                    return 1
                else:
                    return 0

            if (n, index) in memo:
                return memo[(n, index)]
            
            result = findTarget(index + 1, n - nums[index]) + findTarget(index + 1, n + nums[index])
                
            memo[(n, index)] = result
            return result

        return findTarget(0, 0)
        
            