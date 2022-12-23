class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance=float("inf")
        min_index=-1
        for i in range(len(points)):
            if x==points[i][0] or y==points[i][1]:
                distance=abs(x-points[i][0])+abs(y-points[i][1])
                if distance < min_distance:
                    min_index=i
                    min_distance=distance
        return min_index
                
