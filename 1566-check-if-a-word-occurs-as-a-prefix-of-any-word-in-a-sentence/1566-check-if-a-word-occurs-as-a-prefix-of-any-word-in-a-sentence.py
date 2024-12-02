class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        words = sentence.split()
        n = len(searchWord)
        for i in range(len(words)):
            if words[i][:n] == searchWord:
                return i + 1

        return -1


