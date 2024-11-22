class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = nums1 + nums2
        new.sort()
        n = len(new)
        
        if n % 2 == 0:
            median = (new[(n - 1) // 2] + new[((n - 1) // 2) + 1]) / 2
        
        else:
            median = new[n // 2]
        
        return median