class Solution:
    def minimumLength(self, s: str) -> int:
        
        count = Counter(s)
        ans = 0
        for key, val in count.items():
            if val < 3:
                ans += val

            elif val % 2:
                ans += 1

            else:
                ans += 2

        return ans
