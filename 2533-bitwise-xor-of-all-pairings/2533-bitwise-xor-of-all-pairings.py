class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        res1 = 0
        res2 = 0

        for num in nums1:
            res1 ^= num

        for num in nums2:
            res2 ^= num

        ans = 0
        if len(nums1) % 2:
            ans ^= res2

        if len(nums2) % 2:
            ans ^= res1

        return ans
