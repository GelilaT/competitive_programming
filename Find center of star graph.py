class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start,dest in edges:
            graph[start].append(dest)
            graph[dest].append(start)
        
        for i in range(len(graph)):
            if len(graph[i + 1]) == len(graph) - 1:
                return i + 1
            
