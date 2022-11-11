class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        road=[0]*1001
        for passenger,start,end in trips:
            road[start]+=passenger
            road[end]-=passenger
        for i in range(0,len(road)):
            road[i]=road[i]+road[i-1]
            if road[i]>capacity:
                return False
        return True