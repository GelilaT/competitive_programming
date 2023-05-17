class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = {}
        def find(x):
            root = rep.get(x, x)
            if root == x: 
                return x
            rep[x] = find(rep[x])
            return rep[x]

        for start, dest in edges:

            start_rep, dest_rep = find(start), find(dest)
            if start_rep == dest_rep:
                return [start, dest]
            
            rep[start_rep] = dest_rep