class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
       winners={}
       losers={}
       lose=[]
       win=[]
       for i in range(len(matches)):
           if matches[i][0] not in winners:
               winners[matches[i][0]]=1
           else:
               winners[matches[i][0]]+=1
           if matches[i][1] not in losers:
                losers[matches[i][1]]=1
           else:
                losers[matches[i][1]]+=1
       for i in winners.keys():
            if i not in losers:
                win.append(i)
       for i in losers.keys():
            if losers[i]==1:
                lose.append(i)

       lose.sort()
       win.sort()
       return [win,lose]

            
            
        
