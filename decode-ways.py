class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {len(s) : 1}
        def decode(index):
            
            if index in memo:
                return memo[index]

            if s[index] == "0":
                return 0
            
            result = decode(index + 1)
            if index + 1 < len(s):
                if (s[index] == "1") or (s[index] == "2" and s[index + 1] in "0123456"):
                    result += decode(index + 2)
           
            memo[index] = result
            return memo[index]
        
        return decode(0)