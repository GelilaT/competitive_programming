class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        prefix = []
        suffix = [0] * n

        running = 0
        for i in range(n):
            running += nums[i]
            prefix.append(running)

        running = 0
        for i in range(n - 1, -1, -1):
            running += nums[i]
            suffix[i] = running

        ans = 0
        for i in range(n - 1):
            if prefix[i] >= suffix[i + 1]:
                ans += 1

        return ans
