n = int(input())
graph = {}
for i in range(1,n + 1):
    graph[i] = []
for j in range(n):
    line = list(map(int,input().split()))
    for i in range(n):
        if line[i] == 1:
            graph[j + 1].append(i + 1)
source = []
sinks = []
val = []
for i in range(1,n + 1):
    val += graph[i]
val = set(val)
for i in range(1, n + 1):
    if len(graph[i]) == 0:
        sinks.append(i)
    if i not in val:
        source.append(i)
print(len(source),*source)
print(len(sinks),*sinks)


