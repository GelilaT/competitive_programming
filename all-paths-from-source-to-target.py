class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        adj = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adj[i].append(graph[i][j])

        ans = []
        def dfs(node, target, path):
            if node == target:
                ans.append(path.copy() + [node])
                return 
            for neighbour in adj[node]:
                dfs(neighbour, target, path + [node])
        dfs(0, len(graph) - 1, [])
        return ans