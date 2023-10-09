class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1

        # if haystack == needle:
        #     return 0

        n = len(needle)
        lps = [0] * n
        i, j = 0, 1

        while j < len(needle):
            
            if needle[i] == needle[j]:
                lps[j] = i + 1 
                i += 1
                j += 1

            else:
                if i == 0:
                    j += 1

                else:
                    i = lps[i - 1]

        hi, ni = 0, 0
        while hi < len(haystack) and ni < len(needle):

            if needle[ni] == haystack[hi]: 
                ni += 1
                hi += 1

            else:
                if ni == 0:
                    hi += 1
                else:
                    ni = lps[ni - 1]

        if ni == len(needle):
            return hi - n
        else:
            return -1