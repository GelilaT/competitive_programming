from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
        incoming = defaultdict(int)
        
        for start, dest in edges:
            graph[start - 1].append(dest - 1)
            incoming[dest - 1] += 1
            
        queue = deque()
        ans = [-1] * n
        for i in range(n):
            if incoming[i] == 0:
                queue.append((i, 1))
                
         
        while queue:
            cur, time = queue.popleft()
            ans[cur] = time
            
            for neigh in graph[cur]:
                incoming[neigh] -= 1
                
                if incoming[neigh] == 0:
                    queue.append((neigh, time+1))


        return ans
