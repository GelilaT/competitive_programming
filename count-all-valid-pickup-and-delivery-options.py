class Solution:
    def countOrders(self, n: int) -> int:

        slots = 2 * n
        res = 1

        while slots > 0:
            valid = slots * (slots - 1) // 2
            res *= valid
            slots -= 2
        
        return res % (10 ** 9 + 7)