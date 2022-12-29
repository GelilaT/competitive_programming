class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       n=len(word1)
       m=len(word2)
       merged=""
       min_len=min(n,m)
       for inde in range(min_len):
           merged+=word1[inde]
           merged+=word2[inde]
       if n>m:
            merged+=word1[min_len:]
       elif m>n:
            merged+=word2[min_len:]
       return merged
