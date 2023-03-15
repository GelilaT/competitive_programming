class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(left,right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif mid == left == right:
                return -1
            elif mid < 0 or mid > len(nums):
                return -1
            elif nums[mid] > target:
                return helper(left,mid - 1)
            elif nums[mid] < target:
                return helper(mid + 1,right)
        return helper(0,len(nums) - 1)
