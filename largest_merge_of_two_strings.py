class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i=j=0
        n=len(word1)
        m=len(word2)
        merged=""
        
        while i < n and j < m:
            if word1[i:] < word2[j:]:
                merged+=word2[j]
                j+=1
            else:
                merged+=word1[i]
                i+=1
          
        merged+=word1[i:]
        merged+=word2[j:]
        return merged
