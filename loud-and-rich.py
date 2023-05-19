class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0] *len(quiet)

        for start, dest in richer:
            graph[start].append(dest)
            incoming[dest] += 1

        queue = deque()
        ans = [i for i in range(len(quiet))]

        for i in range(len(incoming)):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            cur = queue.popleft()
            cur_min = ans[cur]

            for adj in graph[cur]:
                incoming[adj] -= 1
                if incoming[adj] == 0:
                    queue.append(adj)

                ans[adj] = min(cur_min, ans[adj], key=lambda x : quiet[x])
        return ans