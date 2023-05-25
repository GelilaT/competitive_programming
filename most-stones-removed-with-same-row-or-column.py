class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep = {tuple(point): tuple(point) for point in stones}
        n = len(stones)
        rank = {tuple(point): 1 for point in stones}
        
        def find(x):

            if rep[x] == x:
                return rep[x] 
            rep[x] = find(rep[x])
            return rep[x] 
        
        def union(x, y):

            rootX = find(x)
            rootY = find(y)

            if rank[rootX] == rank[rootY]:
                rank[rootX] += 1
            if rank[rootX] > rank[rootY]:
                rep[rootY] = rootX
            if rank[rootX] < rank[rootY]:
                rep[rootX] = rootY
            
        
        for i in rep:
            for j in rep:
                if i[0] == j[0] or i[1] == j[1]:
                    union(i, j)
        
        parents = set()
        for key in rep:
            parents.add(find(key))

        return n - len(parents)