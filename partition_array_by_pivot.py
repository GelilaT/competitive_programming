class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        #to store numbers less than the pivot
        lower=[]
        #to store numbers more than the pivot
        upper=[]
        #to store numbers equal to the pivot
        equal=[]
        for i in range(n):
            if nums[i] < pivot:
                lower.append(nums[i])
            elif nums[i] == pivot:
                equal.append(nums[i])
            elif nums[i] > pivot:
                upper.append(nums[i])
        return lower+equal+upper
