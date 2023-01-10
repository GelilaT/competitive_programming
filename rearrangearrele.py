class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        rearranged=[]
        for index in range(len(nums)):
            if nums[index] > 0:
                positive.append(nums[index])
            elif nums[index] < 0:
                negative.append(nums[index])
        for index in range(len(positive)):
            rearranged.append(positive[index])
            rearranged.append(negative[index])
        return rearranged
