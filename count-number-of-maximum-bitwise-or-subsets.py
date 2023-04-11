class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        def calculateOR(arr):
            val = 0
            for i in range(len(arr)):
                val |= arr[i]
            return val

        combinations = 0
        def combination(idx, path):

            nonlocal combinations
            if calculateOR(path) == max_or:
                combinations += 2 **(len(nums) - idx)
                return 
            
            if idx == len(nums):
                return

            combination(idx + 1, path + [nums[idx]])
            combination(idx + 1, path)

        combination(0, [])
        return combinations