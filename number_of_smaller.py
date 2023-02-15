n,m=list(map(int,input().split()))
first=list(map(int, input().split()))
second=list(map(int, input().split()))
ans=[]
i=j=0
count=0
while i < m :
    if j < n and second[i] > first[j]:
        count+=1
        j+=1
    else:
        i+=1
        ans.append(count)
print(*ans)
