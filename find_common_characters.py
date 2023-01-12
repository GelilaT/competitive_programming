class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        collection = [200] * 26 
        
        offset = 97
        
        for i in range(len(words)):
            temp = [0] * 26
            for j in range(len(words[i])):
                number = ord(words[i][j]) - offset
                temp[number] += 1
                
            for i in range(26):
                collection[i] = min(collection[i] , temp[i])
                
        output=[]
        
        for i,val in enumerate(collection):
            if val > 0:
                for k in range(val):
                    output.append(chr(i + offset))
                
        return output
