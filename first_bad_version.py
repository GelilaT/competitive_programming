class Solution:
    def firstBadVersion(self, n: int) -> int:

        low=1
        high=n
        mid = ((high - low) // 2) + low
 
        while low < high:
            if isBadVersion(mid):
                high=mid
              
            else:
                low = mid + 1
            mid = ((high - low) // 2) + low

        return mid
            
