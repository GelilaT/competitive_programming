class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        if len(stones) == 1:
            return stones[0]
        for i in range(len(stones)):
            heapq.heappush(arr, -stones[i])
        
        while len(arr) > 1:

            y = -heappop(arr)
            x = -heappop(arr)

            if y > x:
                heappush(arr, -(y - x))
            
        if arr:
            return -arr[0]
        else:
            return 0
