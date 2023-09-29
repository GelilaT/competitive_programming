class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):

        cur = self.root
        for c in word:

            if c not in cur.children:
                cur.children[c] = TrieNode()
                
            cur = cur.children[c]
            cur.count += 1

        cur.is_end = True

    def search(self, word):
        
        cur = self.root
        ans = 0
        for i, c in enumerate(word):

            cur = cur.children[c]
            ans += cur.count

        return ans


class TrieNode:
    def __init__(self):

        self.is_end = False
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = []
        for word in words:
            res = trie.search(word)
            ans.append(res)

        return ans