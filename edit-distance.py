class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}
        def edit(i, j):

            if i >= len(word1) and j >= len(word2):
                return 0

            if i >= len(word1) and j < len(word2):
                return len(word2) - j

            if i < len(word1) and j >= len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = edit(i + 1, j + 1)

            else:
                insert = edit(i, j + 1) 
                delete = edit(i + 1, j) 
                replace = edit(i + 1, j + 1) 
                memo[(i, j)] = min(insert, delete, replace) + 1
    
            return memo[(i, j)]

        return edit(0, 0)