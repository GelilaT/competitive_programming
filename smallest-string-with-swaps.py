class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        rep = [ i for i in range(len(s))]
        groups = [set([i]) for i in range(len(s))]
        rank = [1] * len(s)

        def find(x):

            if rep[x] != x:
                rep[x] = find(rep[x])
            return rep[x]

        def union(x, y):
            repX = find(x)
            repY = find(y)
            if repX == repY:
                return

            if rank[repX] == rank[repY]:
                rank[repX] += 1

            if rank[repX] > rank[repY]:
                rep[repY] = repX
                rank[repY] += 1
                groups[repX].update(groups[repY])
            else:
                rep[repX] = repY
                rank[repY] += 1
                groups[repY].update(groups[repX])

            
        for i in range(len(pairs)):
            union(pairs[i][0], pairs[i][1])
        
        for i in range(len(groups)):
            groups[i] = sorted(groups[i], key=lambda x:s[x])
            groups[i].append(0)
        

        ans = []
        for i in range(len(s)):
            root = find(i)
            tobeused = groups[root][-1]
            next = groups[root][tobeused]
            ans.append(s[next])
            groups[root][-1] += 1
        
        return "".join(ans)