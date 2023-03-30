class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s = x ^ y
        b = bin(s)[2:]
        count = 0
        for i in range(len(b)):
            if b[i] == "1":
                count += 1
        return count
