class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def checker(cur, quantities, n):
            total = 0
            for pro in quantities:
                total += ceil(pro / cur)

            return total > n

        low = 1
        high = sum(quantities)
        while low <= high:
            mid = low + (high - low) // 2
            if checker(mid, quantities, n):
                low = mid + 1

            else:
                high = mid - 1

        return low