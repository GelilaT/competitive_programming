class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        visited = set()
        def dfs(vertex, parent):
            visited.add(vertex)
            
            for child in adj[vertex]:
                if child not in visited:
                    if dfs(child, vertex):
                        return True
                        
                elif child != parent:
                    return True
                    
            return False
		  
        for node in range(len(adj)):
            if node not in visited:
                if dfs(node, -1):
                    return 1
                    
        return 0
