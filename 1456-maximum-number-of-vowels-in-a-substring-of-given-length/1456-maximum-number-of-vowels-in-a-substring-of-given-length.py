class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i=0
        ans=0
        count=0
        for i,char in enumerate(s):
            if char in ("aeiou"):
                count+=1
            if i>=k and s[i-k] in ("aeiou"):
                count-=1
            ans=max(ans,count)
        return ans
