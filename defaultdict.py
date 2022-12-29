from collections import defaultdict
n,m=map(int,input().split())
char_dict=defaultdict(list)
for i in range(n):
    A=input()  
    char_dict[A].append(i+1)
for i in range(m):
    B=input()
    if B in char_dict:
        print(*char_dict[B])
    else:
        print(-1)
