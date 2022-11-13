class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        ans=0
        i=0
        s.lower()
        vowels=["a","e","i","o","u"]
        for j in range(k):
            if s[j] in vowels:
                count+=1
                ans=count
        for j in range(k,len(s)):
            if s[i] in vowels :
                if s[j] not in vowels:
                    ans-=1
            elif s[i] not in vowels:
              if s[j] in vowels:
                ans+=1
            count=max(count,ans)
            i+=1
        return count