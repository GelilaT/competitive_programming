from collections import defaultdict, deque
def parallelCourses(n, pre):
    # Write your code here.
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    for a, b in pre:
        graph[a].append(b)
        indegree[b] += 1

    order = set()
    courses = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            courses.append(i)
            order.add(i)

    count = 0
    while courses:
        length = len(courses)
        for _ in range(length):
            course = courses.popleft()
            for adj in graph[course]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    order.add(adj)
                    courses.append(adj)
            
        count += 1
    if len(order) != n:
        return -1
    return count
