class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * n
        for i in range(len(pre)):
            graph[pre[i][1]].append(pre[i][0])
            in_degree[pre[i][0]] += 1
        
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        courses = []
        while queue:
            node = queue.popleft()
            courses.append(node)
            for adj in graph[node]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)
                
        if len(courses) == n:
            return courses
        else:
            return []