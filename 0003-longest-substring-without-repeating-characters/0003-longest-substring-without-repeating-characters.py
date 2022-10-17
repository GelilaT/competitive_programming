class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        i=0
        res=0
        for j in range(len(s)):
            while s[j] in charset:
                charset.remove(s[i])
                i+=1
            charset.add(s[j])
            res=max(res,j-i+1)
        return res