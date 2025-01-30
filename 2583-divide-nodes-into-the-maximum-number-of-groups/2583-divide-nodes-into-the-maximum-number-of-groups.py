class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        my_dict = defaultdict(int)
        for i in range(1, n + 1):
            q = deque([i])
            dist = [0] * (n + 1)
            dist[i] = maxi = 1
            root = i
            while q:
                a = q.popleft()
                root = min(root, a)
                for b in graph[a]:
                    if dist[b] == 0:
                        dist[b] = dist[a] + 1
                        maxi = max(maxi, dist[b])
                        q.append(b)

                    elif abs(dist[b] - dist[a]) != 1:
                        return -1

            my_dict[root] = max(my_dict[root], maxi)

        return sum(my_dict.values())

        
        