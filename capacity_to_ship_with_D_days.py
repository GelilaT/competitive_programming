class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def max_day(mid):
            day = 1
            capacity = 0
            for weight in weights:
                if capacity + weight >  mid:
                    day += 1
                    capacity = weight 
                else:
                    capacity += weight
            return day
        
        while low < high:

            mid = low + (high - low)//2
            if max_day(mid) <= days:
                high = mid
            else:
                low = mid + 1
        
        return low
