class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, j):
        
        cur = self.root
        for c in word:

            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.is_end = True
        cur.index = j

    

    def search(self, word: str) -> bool:

        cur = self.root
        for c in word:

            if c not in cur.children:
                return -1

            cur = cur.children[c]
        
        def traverse(node):
            
            ans = 0
            if node.is_end:
                ans = max(ans, node.index)

            for child in node.children:
                ans = max(ans, traverse(node.children[child]))
            
            return ans
            
        return traverse(cur)
        
class TrieNode:
    def __init__(self):

        self.is_end = False
        self.children = {}
        self.index = None

class WordFilter:

    def __init__(self, words: List[str]):
        
        self.words = words
        self.trie = Trie()
        for j in range(len(self.words)):
            for i in range(len(self.words[j])):
                self.trie.insert(self.words[j][i:] + '{' + self.words[j], j)

    def f(self, pref: str, suff: str) -> int:
        
        return self.trie.search(suff + '{' + pref)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)