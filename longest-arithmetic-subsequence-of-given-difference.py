class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = {}
        n = len(arr)

        for num in arr:
            cur = num - difference
            dp[num] = dp.get(cur, 0) + 1
        
        return max(dp.values())