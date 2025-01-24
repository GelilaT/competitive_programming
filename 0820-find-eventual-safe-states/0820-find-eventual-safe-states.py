class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        adjacency = defaultdict(list)
        n = len(graph)
        outgoing = [0] * n
        queue = deque()
        ans = []

        for idx, value in enumerate(graph):

            if len(value) == 0:
                queue.append(idx)
                ans.append(idx)
                continue
            for i in range(len(value)):
                adjacency[value[i]].append(idx)
                outgoing[idx] += 1
                
        while queue:
            
            cur = queue.popleft()
            for adj in adjacency[cur]:
                outgoing[adj] -= 1
                if outgoing[adj] == 0:
                    queue.append(adj)
                    ans.append(adj)
        ans.sort()
        return ans

