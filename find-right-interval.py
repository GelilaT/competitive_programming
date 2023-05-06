class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
       nums = sorted(intervals, key=lambda x: x[0])
       ans = [-1] * len(intervals)
       start = {}
       for index, val in enumerate(intervals):
           start[val[0]] = index

       for i in range(len(intervals)):
            index = bisect_left(nums, [intervals[i][1], -float('inf')])
            if index != len(intervals):
                ans[i] = start[nums[index][0]]
       return ans