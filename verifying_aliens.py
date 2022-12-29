class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        print(self.checker("hello","leetcode","hlabcdefgijkmnopqrstuvwxyz"))
        for i in range(len(words)-1):
                if not self.checker(words[i],words[i+1],order):
                    return False
        return True
    def checker(self,word1,word2,order):
        i=0
        minlen=min(len(word1),len(word2))
        isordered=True
        while i < minlen:
            if order.index(word1[i]) < order.index(word2[i]):
                return True
                i+=1
            elif order.index(word1[i]) == order.index(word2[i]):
                i+=1
            else:
                return False
        if len(word1)<=len(word2):
            return True
        else:
            return False
        
            
