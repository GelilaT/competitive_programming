from collections import defaultdict
n = int(input())
graph = defaultdict(list)
matrix = []
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            graph[i].append(j + 1)

for val in graph.values():
    print(len(val), *val)

