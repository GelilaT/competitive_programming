class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        res = ""
        reslen = 0
        for i in range(n):

            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if reslen < r - l + 1:
                    res = s[l: r + 1]
                    reslen = r - l + 1

                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if reslen < r - l + 1:
                    res = s[l: r + 1]
                    reslen = r - l + 1

                l -= 1
                r += 1

        return res 