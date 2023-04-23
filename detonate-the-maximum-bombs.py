class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):      
                if i == j:
                    continue
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                if r1 >= math.sqrt((x1 - x2)**2 + (y1 - y2)**2):
                    graph[i].append(j)
            
        def dfs(node, visited):

            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour, visited)

        max_det = 0
        for i in range(len(bombs)):
            visited = set()
            dfs(i, visited)
            max_det = max(max_det, len(visited))
        return max_det