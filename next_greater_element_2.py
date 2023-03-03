class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        ans = [-1] * len(nums)
        stack = []

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            stack.append(i)

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]

        return ans
