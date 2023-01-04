class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer=[0]*len(nums)
        for index in range(len(nums)):
            answer[index]+=nums[nums[index]]
        return answer
