super_set=set(input().split())
n=int(input())

for i in range(n):
    sets=set(input().split())
    if len(super_set)>len(sets):
        if not sets.issubset(super_set):
            print("False")
            break
else:
    print("True")
