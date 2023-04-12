class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for start,dest in roads:
            graph[start].append(dest)
            graph[dest].append(start)
        
        max_rank = 0
        for i in range(n):
            rank = len(graph[i])
            for j in range(n):
                if j == i:
                    continue
                elif j in graph[i]:
                    max_rank = max(max_rank, rank + len(graph[j]) - 1)
                else:
                    max_rank = max(max_rank, rank + len(graph[j]))
        
        return max_rank