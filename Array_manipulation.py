def arrayManipulation(n, queries):
    
    arr=[0]*(n+1)
    for query in queries:
        start,end,update=query
        arr[start-1]+=update
        arr[end]-=update
    prefix=0
    maxnum=0
    for i in range(len(arr)):
        arr[i]+=prefix
        prefix=arr[i]
        maxnum=max(prefix,maxnum)
    return maxnum
    
