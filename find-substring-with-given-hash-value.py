class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        def find_ord(s):
            return ord(s) - ord('a') + 1

        powers = {0 : 1}
        for i in range(1, len(s)):
            powers[i] = powers[i - 1] * power

        def pollfirst(h, s):

            new_val = (h - (find_ord(s) * powers[k - 1]))  % modulo
            return new_val

        def addlast(h, s):

            new_val = ((power * h) + find_ord(s)) % modulo
            return new_val 

        if len(s) < k:
            return -1
            
        hhash = 0
        i = len(s) - 1
        
        while i >= len(s) - k:
            hhash = addlast(hhash, s[i])
            i -= 1
        
        right = len(s) - 1
        while i > -1:
            if hhash == hashValue:
                ans = s[i + 1 : right + 1]
            
            
            hhash = pollfirst(hhash, s[right])
            hhash = addlast(hhash, s[i])
            
            
            i -= 1
            right -= 1
        
        if hhash == hashValue:
            ans = s[i + 1: right + 1]
        
        return ans