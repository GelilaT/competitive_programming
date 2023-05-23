class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep1 = {i : i for i in s1}
        rep2 = {i : i for i in s2}
        rep3 = {i : i for i in baseStr}
        rep1.update(rep2) 
        rep1.update(rep3)
        rep = rep1
        n, m = len(s1), len(baseStr)
        def find(x):

            if x == rep[x]:
                return rep[x]
            rep[x] = find(rep[x])
            return rep[x]

        def union(x, y):

            rootX = find(x)
            rootY = find(y)
            if rootX < rootY:
                rep[rootY] = rootX
            if rootX > rootY:
                rep[rootX] = rootY

        ans = ''
        for i in range(n):
            union(s1[i], s2[i])
        
        for i in range(m):
            ans += find(baseStr[i])
        
        return ans