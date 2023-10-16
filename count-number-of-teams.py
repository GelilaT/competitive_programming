class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        @cache
        def dp(i, cur, inc):
            
            res = 0
            if cur == 3:
                return 1

            for j in range(i + 1, len(rating)):

                if inc:
                    if rating[j] > rating[i]:
                        res += dp(j, cur + 1, inc)
                
                else:
                    if rating[j] < rating[i]:
                        res += dp(j, cur + 1, inc)

            return res

        res = 0
        for i in range(len(rating)):
            res += dp(i, 1, True)
            res += dp(i, 1, False)

        return res