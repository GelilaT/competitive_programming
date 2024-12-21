class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        if n < 2:
            return 1

        graph = defaultdict(list)
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        vals = [i for i in values]
        queue = deque([i for i in range(n) if degree[i] == 1])
        count = 0

        while queue:
            cur = queue.popleft()
            degree[cur] -= 1
            temp = 0

            if vals[cur] % k == 0:
                count += 1

            else:
                temp = vals[cur]

            for nei in graph[cur]:
                if degree[nei] == 0:
                    continue

                degree[nei] -= 1
                vals[nei] += temp
                if degree[nei] == 1:
                    queue.append(nei)

        return count


        