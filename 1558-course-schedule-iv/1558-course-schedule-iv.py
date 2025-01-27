class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        all_pre = defaultdict(set)
        incoming = [0] * n
        for start, dest in pre:
            graph[start].append(dest)
            incoming[dest] += 1
        
        queue = deque()
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)

        while queue:

            cur = queue.popleft()
            for nei in graph[cur]:
                incoming[nei] -= 1
                all_pre[nei].add(cur)
                all_pre[nei].update(all_pre[cur])
                if incoming[nei] == 0:
                    queue.append(nei)

        res = []
        for start, dest in queries:
            res.append(start in all_pre[dest])
        
        return res
