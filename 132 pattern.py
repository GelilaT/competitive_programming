class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curmin = nums[0]
        for i in range(len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            if stack and stack[-1][0] > nums[i] and nums[i] > stack[-1][1]:
                return True
            stack.append([nums[i], curmin])
            curmin = min(nums[i],curmin)
        
        return False


