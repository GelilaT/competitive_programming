class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = [i for i in range(n)]
        rank = [1] * n
        def representative(x):
            
            if rep[x] == x: 
                return rep[x]
            rep[x] = representative(rep[x])
            return rep[x]
        
        for start,dest in edges:

            start_rep, dest_rep = representative(start), representative(dest) 
            start_rank, dest_rank = rank[start_rep], rank[dest_rep]

            if rank[start_rep] == rank[dest_rep]:
                # start_rank += 1
                rank[start_rep] += 1
            if rank[start_rep] == rank[dest_rep]:
                rep[start_rep] = dest_rep
            else:
                rep[dest_rep] = start_rep
            
        return representative(source) == representative(destination)