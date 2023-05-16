class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incoming = [0] * n
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            incoming[edges[i][1]] += 1
        
        queue = deque()
        ans = [set() for _ in range(n)]
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)
                
        while queue:
            cur = queue.popleft()
            for adj in graph[cur]:
                ans[adj].add(cur)
                ans[adj] = ans[adj].union(ans[cur])
                incoming[adj] -= 1
                if incoming[adj] == 0:
                    ans[adj] = sorted(list(ans[adj]))
                    queue.append(adj)

        return ans