def pile(sidelength):
    left=0
    right=len(sidelength)-1
    current=float('inf')
    while left<=right:
        if sidelength[left]<=sidelength[right]<=current:
            current=sidelength[right]
            right-=1
        elif sidelength[right]<sidelength[left]<=current:
            current=sidelength[left]
            left+=1
        else:
            return "No"
    return "Yes"
testcase=int(input())
for i in range(testcase):
    n=int(input())
    sidelength=[int(length) for length in input().split()]
    print(pile(sidelength))
