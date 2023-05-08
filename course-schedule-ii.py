class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        color = [0] * n
        for i in range(len(pre)):
            graph[pre[i][1]].append(pre[i][0])

        ans = []
        cyclic = False
        def dfs(node):
            nonlocal color
            nonlocal ans
            nonlocal cyclic
            for adj in graph[node]:
                if color[adj] == 0:
                    color[adj] = 1
                    dfs(adj)
                elif color[adj] == 1:
                    cyclic = True
                    return 
             
            color[node] = 2
            ans.append(node)
        
        for i in range(n):
            if cyclic:
                return []
            if color[i] == 0:
                dfs(i)
        return ans[::-1]