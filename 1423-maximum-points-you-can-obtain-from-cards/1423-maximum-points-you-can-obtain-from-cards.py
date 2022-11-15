class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
          n=len(cardPoints)
          totalpts=sum(cardPoints)
          i=0
          cursum=0
          ans=0
          for j in range(n-k):
            cursum+=cardPoints[j]
          ans=max(ans,totalpts-cursum)
          for j in range(n-k,n):
            cursum=cursum-cardPoints[i]+cardPoints[j]
            ans=max(ans,totalpts-cursum)
            i+=1
          return ans