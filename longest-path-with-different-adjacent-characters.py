class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        path = 1
        graph = defaultdict(list)
        for i in range(1, len(parent)):
            graph[parent[i]].append(i)

        def dfs(root):

            nonlocal path
            # if root not in graph:
            #     return 1
            
            ans = 1
            for child in graph[root]:
                length = dfs(child)

                if s[root] != s[child]:
                    path = max(path, length + ans)
                    ans = max(ans, length + 1)
            
            return ans
        dfs(0)
        return path