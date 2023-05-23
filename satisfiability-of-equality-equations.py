class Solution:
    def equationsPossible(self, equ: List[str]) -> bool:
        rep = {}
        n = len(equ)
        rank = {}
        for i in range(n):
            rep[equ[i][0]] = equ[i][0]
            rep[equ[i][-1]] = equ[i][-1]
            rank[equ[i][0]] = 1
            rank[equ[i][-1]] = 1

        def find(x):

            if rep[x] == x:
                return rep[x]
            rep[x] = find(rep[x])
            return rep[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return 0
            if rank[rootX] > rank[rootY]:
                rep[rootY] = rootX
            if rank[rootX] < rank[rootY]:
                rep[rootX] = rootY
            if rank[rootX] == rank[rootY]:
                rank[rootX] += 1
                rep[rootX] = rootY
                
        for i in range(n):
            if equ[i][1] == "=":
                union(equ[i][0], equ[i][-1])

        for i in range(n):
            rootX = find(equ[i][0])
            rootY = find(equ[i][-1])
            if equ[i][1] == "=" and rootX != rootY:
                return False
            if equ[i][1] == "!" and rootX == rootY:
                return False
        return True