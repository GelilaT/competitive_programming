class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        s1_dict={}
        s2_dict={}
        if k > len(s2):
            return False
        for i in range(k):
            
            s1_dict[s1[i]]= 1 + s1_dict.get(s1[i],0)
            s2_dict[s2[i]]= 1 + s2_dict.get(s2[i],0)

        start=0
        if s1_dict == s2_dict:
            return True
        for i in range(k,len(s2)):
            if s2[start] != s2[i]:
                s2_dict[s2[start]]-=1
                s2_dict[s2[i]] = 1 + s2_dict.get(s2[i],0)

            if s2_dict[s2[start]] == 0:
                del s2_dict[s2[start]]

            start+=1
            if s1_dict == s2_dict:
               return True
        
        return False

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
