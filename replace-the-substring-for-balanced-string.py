class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        ans = n = len(s)
        i = 0

        for j, char in enumerate(s):
            
            count[char] -= 1
            while i < n and all(n / 4 >= count[char] for char in 'QWER'):
                ans = min(ans, j - i + 1)
                count[s[i]] += 1
                i += 1

        return ans