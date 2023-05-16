class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for start,dest in edges:
            graph[start].append(dest)
            # graph[dest].append(start)
        
        ans = [0] * n
        def dfs(node):
            # start = count(labels[node])
            # node_cnt = defaultdict(list)
            count = 1
            for neighbour in graph[node]:
                if labels[node] == labels[neighbour]:
                    count += dfs(neighbour)
                else: 
                    dfs(neighbour)
            ans[node] = count
            return count
        dfs(0)
        return ans