class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited = [0 for i in range(n + 1)]
        color = [0 for i in range(n + 1)]
        graph = defaultdict(list)
        for start,dest in dislikes:
            graph[start].append(dest)
            graph[dest].append(start)


        def dfs(node, visited, color):

            for neighbour in graph[node]:
                if visited[neighbour] == False:
                    visited[neighbour] = True
                    color[neighbour] = not color[node]

                    if not dfs(neighbour, visited, color):
                        return False
                    
                elif color[neighbour] == color[node]:
                    return False

            return True
        res = True
        for i in range(1, n + 1):
            res = res and dfs(i, visited, color)
        return res