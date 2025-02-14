class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]

        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # [1, 1, 2, 6, 24]
        # [3, 0, 2, 5, 4]
        # [1, 3, 0, 2, 10, 40]
        n = len(self.prefix)
        if n <= k:
            return 0

        return self.prefix[-1] // self.prefix[n - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)