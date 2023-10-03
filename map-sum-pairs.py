class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:

        count = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root

        for char in key:
            cur = cur.children[char]
            cur.value += count

    def sum(self, prefix: str) -> int:
        
        cur = self.root

        for char in prefix:
            cur = cur.children.get(char)

            if not cur:
                return 0

        return cur.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)