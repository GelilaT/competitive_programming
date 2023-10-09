class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def find_ord(s):
            return ord(s) - ord('a') + 1

        def convert(word):
            val = 0
            
            for i in range(len(word) - 1, -1, -1):
                val += find_ord(word[i]) * (27 ** (len(word) - (i + 1)))

            return val

        def pollfirst(h, k, s):

            new_val = h - (find_ord(s) * (27 ** (k - 1)))
            return new_val

        def addlast(h, s):

            new_val = 27 * h + find_ord(s)
            return new_val

        i = 0
        k = len(needle)
        n = convert(needle)
        h = convert(haystack[i: k])

        if n == h:
            return 0

        l, r = 0, k
        while r < len(haystack):

            if n == h:
                return l

            h = pollfirst(h, k, haystack[l])
            h = addlast(h, haystack[r])

            l += 1
            r += 1
        
        if n == h:
            return l
        else:
            return -1