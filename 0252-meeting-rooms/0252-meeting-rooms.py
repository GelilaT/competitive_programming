class Solution:
    def canAttendMeetings(self, meetings: List[List[int]]) -> bool:
        
        meetings.sort()
        for i in range(len(meetings) - 1):
            if meetings[i][1] > meetings[i + 1][0]:
                return False
            
        return True
        