class MyHashMap:

    def __init__(self):
        self.my_dict = {}

    def put(self, key: int, value: int) -> None:
            self.my_dict[key] = value

    def get(self, key: int) -> int:
        
        if key in self.my_dict:
            return self.my_dict[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.my_dict:
            del self.my_dict[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)