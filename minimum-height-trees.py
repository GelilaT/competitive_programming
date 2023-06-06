class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        incoming = [0] * n
        if n == 1:
            return [0]
            
        for start,dest in edges:
            graph[start].append(dest)
            graph[dest].append(start)
            incoming[dest] += 1
            incoming[start] += 1

        queue = deque() 
        for i in range(n):
            if incoming[i] == 1:
                queue.append(i)
            
        while queue:
            length = len(queue)
            ans = []
            for i in range(length):
                cur = queue.popleft()
                ans.append(cur)
                for adj in graph[cur]:
                    incoming[adj] -= 1
                    if incoming[adj] == 1:
                        queue.append(adj)

        return ans