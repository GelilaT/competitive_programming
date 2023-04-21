class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums):
            count = 0
            if len(nums) > 1:
                mid = len(nums) // 2
                left = nums[:mid]
                right = nums[mid:]
                count = count + mergeSort(left) + mergeSort(right)
                idx = 0
                for i in range(len(left)):
                    while idx < len(right) and left[i] > right[idx] * 2:
                        idx += 1
                    count += idx
                l, r, i = 0, 0, 0
                while l < len(left) and r < len(right):
                    if left[l] > right[r]:
                        nums[i] = right[r]
                        r += 1
                    else:
                        nums[i] = left[l]
                        l += 1
                    i += 1
                while l < len(left):
                    nums[i] = left[l]
                    i += 1
                    l += 1
                while r < len(right):
                    nums[i] = right[r]
                    i += 1
                    r += 1
            return count
        return mergeSort(nums)