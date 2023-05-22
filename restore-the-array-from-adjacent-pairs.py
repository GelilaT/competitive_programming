class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        n = len(adjacentPairs)
        for start, dest in adjacentPairs:
            graph[start].append(dest)
            graph[dest].append(start)

        queue = deque()
        visited = set()
        ans = []
        for key in graph.keys():
            if len(graph[key]) == 1:
                queue.append(key)
                visited.add(key)
                ans.append(key)
                break

        while queue:
            cur = queue.popleft()
            for adj in graph[cur]:
                if adj not in visited:
                    ans.append(adj)
                    visited.add(adj)
                    queue.append(adj)

        return ans