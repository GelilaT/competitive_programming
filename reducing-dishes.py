class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        n = len(satisfaction)
        ans, sum, coef = 0, 0, 0

        for i in range(n - 1, -1, -1):
            if sum + satisfaction[i] > 0:
                sum += satisfaction[i]
                coef += sum
                ans = max(ans, coef)

        return ans