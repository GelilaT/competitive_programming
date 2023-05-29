class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        for start,dest in edges:
            graph[start].append(dest)
            graph[dest].append(start)

        def dfs(cur, par):
            time = 0
            for adj in graph[cur]:
                if adj == par:
                    continue
                adj_time = dfs(adj, cur)
                if adj_time or hasApple[adj]:
                    time += 2 + adj_time
            return time
        return dfs(0, -1)