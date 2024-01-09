t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mn, mx = 0, 10**9
    for j in range(n - 1):
        x, y = a[j], a[j + 1]
        midL = (x + y) // 2
        midR = (x + y + 1) // 2
        if x < y:
            mx = min(mx, midL)
        if x > y:
            mn = max(mn, midR)
    if mn <= mx:
        print(mn)
    else:
        print(-1)
