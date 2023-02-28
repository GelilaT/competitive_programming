class MyCircularDeque:

    def __init__(self, k: int):
        self.list=[]
        self.k=k

    def insertFront(self, value: int) -> bool:
        if len(self.list) < self.k:
            self.list = [value] + self.list
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.list) < self.k:
            self.list.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.list:
            self.list.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if self.list:
            self.list.pop()
            return True
        return False
        
    def getFront(self) -> int:
        if self.list:
            return self.list[0]
        return -1

    def getRear(self) -> int:
        if self.list:
            return self.list[-1]
        return -1

    def isEmpty(self) -> bool:
        if self.list:
            return False
        return True

    def isFull(self) -> bool:
        if len(self.list) == self.k:
            return True
        return False
