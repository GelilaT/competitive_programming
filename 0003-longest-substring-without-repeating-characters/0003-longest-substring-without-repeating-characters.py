class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j=ans=0
        charset=set()
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[j])
                j+=1
            charset.add(s[i])
            ans=max(ans,i-j+1)
        return ans