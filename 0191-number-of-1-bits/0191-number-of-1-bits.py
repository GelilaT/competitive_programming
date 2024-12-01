class Solution:
    def hammingWeight(self, n: int) -> int:
        
        inbits = bin(n)
        ans = 0
        for i in range(2, len(inbits)):
            if inbits[i] == "1":
                ans += 1 

        return ans