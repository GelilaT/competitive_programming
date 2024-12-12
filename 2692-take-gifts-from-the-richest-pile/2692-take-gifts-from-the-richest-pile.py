class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        heap = []
        for i in gifts:
            heappush(heap, -i)

        for i in range(k):
            curMax = heappop(heap)
            square = floor(sqrt(-curMax))
            heappush(heap, -square)

        return -sum(heap)
