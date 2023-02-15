t=int(input())
for i in range(t):
    n=int(input())
    length=n
    arr=list(map(int, input().split()))
    ptr=1
    arr.sort()
    while ptr < n:
        if abs(arr[ptr]-arr[ptr-1]) == 1 or arr[ptr] == arr[ptr-1]:
            length-=1
            ptr+=1
        else:
            ptr+=1
    if length == 1 or n == 1:
        print("YES")
    else:
        print("NO")
        

