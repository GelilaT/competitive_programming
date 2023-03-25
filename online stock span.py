class StockSpanner:

    def __init__(self):
        
        self.stock = []

    def next(self, price: int) -> int:
    #    print(self.stock,self.count) 
       count = 1
       while self.stock and self.stock[-1][0] <= price:
           count += self.stock[-1][1]
           self.stock.pop()
    #    print(self.stock,self.count)
       self.stock.append([price,count])
       return count
