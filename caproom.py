k=int(input())
roomnum=input().split()
def capnum(roomnum,k):
    roomnum=[int(x) for x in roomnum]
    roomnum=sorted(roomnum)
    i=0
    while i<len(roomnum):
        try:
            if roomnum[i]==roomnum[i+1]:
                i+=k
            else:
                return roomnum[i]
        except:
            return roomnum[-1]
print(capnum(roomnum,k))
