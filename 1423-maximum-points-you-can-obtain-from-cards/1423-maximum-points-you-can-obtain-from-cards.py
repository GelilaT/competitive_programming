class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i,j=0,len(cardPoints)-k
        total=sum(cardPoints[j:])
        ans=total
        while j<len(cardPoints):
          total+=(cardPoints[i]-cardPoints[j]) 
          ans=max(ans,total)
          i+=1
          j+=1
        return ans