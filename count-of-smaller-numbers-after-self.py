class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        arr = sorted(nums)
        count = []

        for num in nums:
            index = bisect_left(arr, num)
            count.append(index)
            del arr[index]
        
        return count