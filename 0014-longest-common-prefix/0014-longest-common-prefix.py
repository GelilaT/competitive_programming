class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, words):

        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()

                cur = cur.children[c]
            cur.is_end = True

    def startswith(self, word):
        
        ans = ""
        cur = self.root
        for c in word:
            if len(cur.children) != 1 or cur.is_end:
                return ans
            ans += c
            cur = cur.children[c]
        return ans

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        trie.insert(strs)
        ans = trie.startswith(strs[0])
        return ans