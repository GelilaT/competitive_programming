from collections import defaultdict
n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int, input().split()))
    letters=input()
    my_dict=defaultdict(list)
    result=True
    for index,val in enumerate(a):
        my_dict[val].append(index)
    for val in my_dict.values():
        if len(val)>1:
            letter=letters[val[0]]
            for index in range(1,len(val)):
                if letter!=letters[val[index]]:
                    print("No")
                    result=False
                    break 
        if not result:
            break
    if result:
        print("Yes")
