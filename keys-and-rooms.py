class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            graph[i] += rooms[i]
        
        def bfs(start):
            queue = deque([start])
            visited = set([start])

            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            if len(visited) == len(graph):
                return True
            else:
                return False
            # return visited
        return bfs(0)