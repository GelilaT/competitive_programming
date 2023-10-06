class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for start, dest, cost in flights:
            graph[start].append([dest, cost])

        heap = [[0, src, 0]]
        visited = {}
        costs = [inf] * (n + 1)
        costs[src] = 0

        while heap:
            # print(heap)
            cost, city, count = heappop(heap)
            visited[city] = count
            if city == dst and count - 1 <= k:
                return cost

            for d, c in graph[city]:
                new_cost = cost + c
                
                if d not in visited or visited[d] > count:
                    heappush(heap, [new_cost, d, count + 1])

        return -1