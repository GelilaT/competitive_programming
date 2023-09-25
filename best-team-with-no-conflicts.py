class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        arr = zip(scores, ages)
        arr = sorted(arr)

        dp = [arr[i][0] for i in range(len(ages))]

        for j in range(len(arr)):
            max_score, max_age = arr[j]

            for i in range(0, j):
                score, age = arr[i]
                if max_age >= age:
                    dp[j] = max(max_score + dp[i], dp[j])

        return max(dp)