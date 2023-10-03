class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for start, dest, time in times:
            graph[start].append([time, dest])

        heap = [[0, k]]
        visited = set()
        costs = [inf] * n
        costs[k - 1] = 0
        while heap:

            cost, node = heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            for c, dest in graph[node]:
                new_cost = cost + c

                if new_cost < costs[dest - 1]:
                    costs[dest - 1] = new_cost
                    heappush(heap, [new_cost, dest])

        if len(visited) != n:
            return -1
        
        ans = 0
        for cost in costs:
            if cost != inf:
                ans = max(ans, cost)
        
        return ans