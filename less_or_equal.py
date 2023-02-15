n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
arr.sort()
if k < n and arr[k-1] < arr[k]:
    print(arr[k-1])
elif k == n:
    print(arr[-1])
elif k == 0 and arr[0] > 1:
    print(arr[0] - 1)
else:
    print(-1)
