class Solution:
    def getDiameter(self, graph, nodes):
        def bfs(start):
            dist = [-1] * nodes
            q = deque([start])
            dist[start] = 0
            farNode = start

            while q:
                curr = q.popleft()

                for nei in graph[curr]:
                    if dist[nei] == -1:
                        dist[nei] = dist[curr] + 1
                        q.append(nei)
                        
                        if dist[nei] > dist[farNode]:
                            farNode = nei

            return farNode, dist[farNode]
        
        return bfs(bfs(0)[0])[1]

    def minimumDiameterAfterMerge(self, tree1, tree2):
        n, m = len(tree1) + 1, len(tree2) + 1
        g1, g2 = [[] for _ in range(n)], [[] for _ in range(m)]
        
        for a, b in tree1:
            g1[a].append(b)
            g1[b].append(a)

        for a, b in tree2:
            g2[a].append(b)
            g2[b].append(a)
        
        d1 = self.getDiameter(g1, n)
        d2 = self.getDiameter(g2, m)

        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)