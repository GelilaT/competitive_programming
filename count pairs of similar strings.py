class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter=0
        for i in range(len(words)-1):
            count1=collections.Counter(words[i])
            for j in range(i+1,len(words)):
                count2=collections.Counter(words[j])
                if count1.keys()==count2.keys():
                    counter+=1
        return counter
                
                
