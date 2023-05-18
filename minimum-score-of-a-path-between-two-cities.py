class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        min_cost = [inf for _ in range(n + 1)]
        def find(x):

            if rep[x] == x:
                return rep[x]
            rep[x] = find(rep[x])
            return rep[x]

        for start, dest, cost in roads:
        
            start_rep, dest_rep = find(start), find(dest)
            minn = min(min_cost[start_rep], min_cost[dest_rep], cost)

            if rank[start_rep] == rank[dest_rep]:
                rank[start_rep] += 1
            if rank[start_rep] < rank[dest_rep]:
                rep[start_rep] = dest_rep
                min_cost[dest_rep] = minn
            else:
                rep[dest_rep] = start_rep
                min_cost[start_rep] = minn

        return min_cost[find(1)]