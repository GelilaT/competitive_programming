class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        heap = []
        for i in range(len(piles)):
            heappush(heap, -piles[i])
        print(heap)
        for i in range(k):
            heappush(heap, heap[0] + (-heappop(heap) // 2))

        return -sum(heap)