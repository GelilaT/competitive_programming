n = int(input())
arr = list(map(int, input().split()))
odd = even = False
for num in arr:
    if num % 2 == 0:
        even = True
    elif num % 2 != 0:
        odd = True

if odd and even:
    arr.sort()
    print(*arr)
else:
    print(*arr)
