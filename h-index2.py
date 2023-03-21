class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right = 0, len(citations)
        n = len(citations)
        while left <= right:
            mid = (right + left) // 2
            idx = bisect_left(citations, mid)
            if mid <= n - idx:
                left = mid + 1
            else:
                right = mid - 1
        return right
