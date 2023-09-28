class TrieNode:
    def __init__(self):

        self.is_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        
        cur = self.root
        for c in word:

            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.is_end = True

    def search(self, word: str) -> bool:
        
        def traverse(i, node):

            if i == len(word) and node.is_end:
                return True
            
            while i < len(word) and word[i] != '.':
                
                if word[i] not in node.children:
                    return False

                node = node.children[word[i]]
                i += 1
                if i == len(word):
                    if node.is_end:
                        return True
                    return False

            for child in node.children:
                if traverse(i + 1, node.children[child]):
                    return True
            
            return False

        return traverse(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)