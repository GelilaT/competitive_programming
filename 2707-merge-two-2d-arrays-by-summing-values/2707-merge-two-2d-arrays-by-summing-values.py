class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        my_dict = defaultdict(int)
        for ids, num in nums1:
            my_dict[ids] += num

        for ids, num in nums2:
            my_dict[ids] += num

        ans = []
        for key, val in my_dict.items():
            ans.append([key, val])

        ans.sort()
        return ans

