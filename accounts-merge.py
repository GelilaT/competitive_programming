class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        rep = [i for i in range(len(accounts))]
        my_dict = {}
        rank = [1] * len(accounts)

        def find(x):
            if x == rep[x]:
                return rep[x]
            rep[x] = find(rep[x])
            return rep[x]

        def union(x, y):
            repX, repY = find(x), find(y)
            if repX == repY:
                return
            if rank[repX] == rank[repY]:
                rank[repX] += 1
            if rank[repX] < rank[repY]:
                rep[repX] = repY
            else:
                rep[repY] = repX

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                em = accounts[i][j]
                if em not in my_dict:
                    my_dict[em] = i
                else:
                    union(i, my_dict[em])
        
        temp = defaultdict(list)
        for key, val in my_dict.items():
            root = find(val)
            temp[root].append(key)
        
        ans = []
        for val in temp:
            new_val = sorted(temp[val])
            res = [accounts[val][0]]
            res.extend(new_val)
            ans.append(res)
        return ans