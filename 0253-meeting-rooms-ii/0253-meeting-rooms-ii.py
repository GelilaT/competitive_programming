class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        heap = []
        intervals.sort()
        count = 0
        
        for start, end in intervals:
            while heap and start >= heap[0]:
                heappop(heap)
                
            heappush(heap, end)
            count = max(count, len(heap))
            
        return count