class Solution:
    def countPairs(self, food: List[int]) -> int:
        good=0
        poweroftwo=[]
        previous={food[0]:1}
        for i in range(22):
            poweroftwo.append(2**i)
        for j in range(1,len(food)):
            for x in range(len(poweroftwo)):
                diff=poweroftwo[x]-food[j]
                if diff in previous:
                    good+=previous[diff]
            previous[food[j]]=previous.get(food[j],0)+1
        return good %(10**9+7)
