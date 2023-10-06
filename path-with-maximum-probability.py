class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for i in range(len(edges)):
            start = edges[i][0]
            dest = edges[i][1]
            graph[start].append([dest, succProb[i]])
            graph[dest].append([start, succProb[i]])

        heap = [[-1, start_node]]
        visited = set()
        probs = [float('inf')] * n
        
        while heap:

            prob, node = heappop(heap)
            if node == end_node:
                return -prob

            if node in visited:
                continue

            visited.add(node)
            for child, sprob in graph[node]:
                new_prob = prob * sprob

                if new_prob < probs[child]:
                    probs[child] = new_prob
                    heappush(heap, [new_prob, child])

        return 0