from collections import defaultdict
graph = defaultdict(list)
n = int(input())
k = int(input())
for _ in range(k):
    op = list(map(int, input().split()))
    if op[0] == 1:
        graph[op[1]].append(op[2])
        graph[op[2]].append(op[1])
    if op[0] == 2:
        print(*graph[op[1]])


    

