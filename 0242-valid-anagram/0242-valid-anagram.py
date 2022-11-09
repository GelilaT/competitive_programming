class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
         from collections import Counter
         ci=Counter(s1)
         if len(s1)!=len(s2):
             return False
         return Counter(s1)==Counter(s2)