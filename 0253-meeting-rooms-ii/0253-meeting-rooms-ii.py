class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        maxi = 0
        for start, end in intervals:
            maxi = max(maxi, end)
            
        prefix = [0] * (maxi + 1)
        for start, end in intervals:
            prefix[start] += 1
            prefix[end] -= 1
            
        for i in range(1, maxi):
            prefix[i] = prefix[i] + prefix[i - 1]
            
        return max(prefix)