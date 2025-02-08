class NumberContainers(object):

    def __init__(self):
        self.indices = {}
        self.nums = defaultdict(SortedSet)

    def change(self, index, number):
        
        if index in self.indices : 
            if self.indices[index] == number: 
                return 
            prev = self.indices [index]
            self.nums[prev].remove(index)
        
        self.nums[number].add(index)
        self.indices[index] = number


    def find(self, number):
    
        if number not in self.nums or not self.nums[number]:
            return -1
        return self.nums[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)