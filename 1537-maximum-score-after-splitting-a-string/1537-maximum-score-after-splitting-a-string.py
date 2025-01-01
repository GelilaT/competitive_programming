class Solution:
    def maxScore(self, s: str) -> int:
        
        n = len(s)
        prefix = []
        running = 0
        for i in range(n):
            running += int(s[i])
            prefix.append(running)

        suffix = [0] * n
        running = 0
        for i in range(n - 1, -1, -1):
            running += int(s[i])
            suffix[i] = running 

        ans = 0
        for i in range(n - 1):
            cur_sum = i + 1 - prefix[i] + suffix[i + 1]
            ans = max(ans, cur_sum)

        return ans
