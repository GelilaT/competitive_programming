class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for start,dest in edges:
            graph[start].append(dest)

        ans = []
        values = []
        for val in graph.values():
            values += val
        values = set(values)
        # print(values)

        for i in range(n):
            if i not in values:
                ans.append(i)

        return ans
