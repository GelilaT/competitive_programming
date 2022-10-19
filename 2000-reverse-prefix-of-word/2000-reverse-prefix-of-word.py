class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans=""
        new=""
        for i in range(len(word)):
            if word[i]==ch:
                new+=word[i::-1]
                break
            i+=1
        if new:
           ans=new+word[i+1::]
           return ans
        else:
            ans=word
            return ans
        
           
