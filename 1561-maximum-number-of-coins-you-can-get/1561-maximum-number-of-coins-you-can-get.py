class Solution(object):
    def maxCoins(self, piles):
         piles=sorted(piles)
         n=len(piles)
         pile=[]
         total=0
         while piles :
           pile.append(piles.pop())
           pile.append(piles.pop())
           pile.append(piles.pop(0))
         for k in range(1,len(pile),3):
            total+=pile[k]
         return total