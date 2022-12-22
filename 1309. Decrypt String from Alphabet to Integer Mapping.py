class Solution:
    def freqAlphabets(self, s: str) -> str:
        output=""
        i=0
        while i<len(s):
            if i+2<len(s) and s[i+2]=="#":
                order=int(s[i:i+2])
                output+=chr(order+96)
                i+=3
            else:
                output+=chr(int(s[i])+96)
                i+=1
        return output
