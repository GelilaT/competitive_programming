class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        lower=[]
        upper=[]
        equal=[]
        for i in range(n):
            if nums[i] < pivot:
                lower.append(nums[i])
            elif nums[i] == pivot:
                equal.append(nums[i])
            elif nums[i] > pivot:
                upper.append(nums[i])
        return lower+equal+upper