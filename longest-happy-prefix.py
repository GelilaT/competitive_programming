class Solution:
    def longestPrefix(self, s: str) -> str:
        
        n = len(s)
        lps = [0] * n
        i, j = 0, 1

        while j < len(s):

            if s[i] == s[j]:
                lps[j] = i + 1
                i += 1
                j += 1

            else:
                if i == 0:
                    j += 1
                else:
                    i = lps[i - 1]

        if lps[-1] == 0:
            return ''
        else:
            return s[(n - 1) - lps[-1] + 1: (n - 1) + 1]