class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * n
        for i in range(len(pre)):
            graph[pre[i][0]].append(pre[i][1])
            indegree[pre[i][1]] += 1
        
        courses = deque()
        for i in range(n):
            if indegree[i] == 0:
                courses.append(i)
        order = []
        while courses:
            nxt_course = courses.popleft()
            order.append(nxt_course)
            for adj in graph[nxt_course]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    courses.append(adj)
        if len(order) == n:
            return True
        else:
            return False