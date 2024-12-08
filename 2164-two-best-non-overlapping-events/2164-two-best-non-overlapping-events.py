class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        heap = []
        maxVal = res = 0

        for start, end, val in events:
            while heap and heap[0][0] < start:
                maxVal = max(maxVal, heappop(heap)[2])

            res = max(res, maxVal + val)
            heappush(heap, (end, start, val))

        return res
        

        
        






        