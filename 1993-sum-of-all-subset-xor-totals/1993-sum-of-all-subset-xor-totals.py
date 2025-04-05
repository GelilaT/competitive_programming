class Solution:
    def subsetXORSum(self, nums):
        
        self.result = 0                  
        def dfs(index, current_xor):
            if index == len(nums):
                self.result += current_xor  
                return                     

            dfs(index + 1, current_xor)

            dfs(index + 1, current_xor ^ nums[index])

        dfs(0, 0)

        return self.result