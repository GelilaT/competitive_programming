class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def allowed(speed):
            hours=0
            for pile in piles:
                hours += ceil(pile / speed)
            
            return hours <= h

        low, high = 1, max(piles)
        while low < high:
            mid = low + (high - low) // 2
            if allowed(mid):
                high = mid
            else:
                low = mid + 1

        return low
