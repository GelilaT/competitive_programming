n,m=list(map(int,input().split()))
first=list(map(int, input().split()))
second=list(map(int, input().split()))
ans=[]
i=j=0
while i < n and j < m:
    if first[i] <= second[j]:
        ans.append(first[i])
        i+=1
    else:
        ans.append(second[j])
        j+=1
ans.extend(first[i:])
ans.extend(second[j:])
print(*ans)
