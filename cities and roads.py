n = int(input())
matrix = []
count = 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(i):
        count += row[j]
print(count)
