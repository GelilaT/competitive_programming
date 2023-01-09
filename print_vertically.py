class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr=s.split(" ")
        maxlen=0
        newarr=[]
        for i in range(len(arr)):
            maxlen=max(maxlen,len(arr[i]))
        for j in range(maxlen):
            new=""
            final=""
            for i in range(len(arr)):
                try:
                    new+=arr[i][j]
                except:
                    new+=" "
            for index in range(len(new)-1,-1,-1):
                if new[index]!=" ":
                    charidx=index
                    break
            newarr.append(new[:charidx+1])
        return newarr
