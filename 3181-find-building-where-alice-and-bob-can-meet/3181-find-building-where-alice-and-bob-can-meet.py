class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        n, q = len(heights), len(queries)
        res = [-1] * q
        diff = [[] for _ in range(n)]
        heap = []
        for i in range(len(queries)):
            a, b = queries[i]
            
            if a > b:
                a, b = b, a

            if a == b or heights[a] < heights[b]:
                res[i] = b
            else:
                diff[b].append((heights[a], i))

        for i in range(n):
            for query in diff[i]:
                heappush(heap, query)
            while heap and heap[0][0] < heights[i]:
                res[heap[0][1]] = i
                heappop(heap)

        return res

        