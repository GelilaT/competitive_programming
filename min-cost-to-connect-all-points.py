class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [[] for _ in range(n)]
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                graph[i].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j))
                graph[j].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i))

        heap = [(0, 0)]
        res, visited = 0, set()

        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            res += cost

            for c, point in graph[node]:
                heapq.heappush(heap, (c, point))
            
            if len(visited) == n:
                return res