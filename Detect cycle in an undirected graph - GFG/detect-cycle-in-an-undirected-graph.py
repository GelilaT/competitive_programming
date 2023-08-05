from typing import List
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

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends