class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        queue = deque([source])
        visited = set()
        graph = defaultdict(list)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                graph[routes[i][j]].append(i)

        ans = -1
        while queue:
            ans += 1
            for _ in range(len(queue)):
                stop = queue.popleft()
                if stop == target:
                    return ans
                
                for bus in graph[stop]:
                    if bus not in visited:
                        visited.add(bus)
                        queue.extend(routes[bus])
                    
        return -1