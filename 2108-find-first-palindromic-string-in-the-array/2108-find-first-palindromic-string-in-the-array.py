class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        new=[]
        for i in range(len(words)):
            reverse=words[i][::-1]
            if reverse==words[i]:
                new.append(reverse)
        if new:
            return new[0]
        return ""   
                