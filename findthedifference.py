class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        count = Counter(s)
        for i,char in enumerate(t):
            count[char] -= 1
            if count[char] == -1:
                return char
