class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        limit=int(sqrt(c))
        left=0
        right=limit
        while left <= right:
            first=left**2
            second=right**2
            sum=first+second
            if sum > c:
                right-=1
            elif sum < c:
                left+=1
            else:
                return True
        return False
