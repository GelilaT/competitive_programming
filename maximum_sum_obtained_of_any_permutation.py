class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        range_arr=[0] * (n+1)
        for request in requests:
            start = request[0]
            end = request[1]
            range_arr[start] += 1
            range_arr[end + 1] -= 1
        prefix_arr = []
        prefix = 0
        for i in range(n):
            prefix += range_arr[i]
            prefix_arr.append(prefix)
        prefix_arr.sort()
        nums.sort()
        ans = 0
        mod=(10 ** 9) + 7
        for i in range(n):
            ans += prefix_arr[i] * nums[i]
        return ans % mod
