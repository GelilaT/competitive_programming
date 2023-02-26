class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      
        k=len(p)
        ans=[]
        p_dict={}
        s_dict={}
        if k > len(s):
            return []
        for i in range(k):
            
            p_dict[p[i]]= 1 + p_dict.get(p[i],0)
            s_dict[s[i]]= 1 + s_dict.get(s[i],0)

        start=0
        if p_dict == s_dict:
            ans.append(start)
        for i in range(k,len(s)):
            if s[start] != s[i]:
                s_dict[s[start]]-=1
                s_dict[s[i]] = 1 + s_dict.get(s[i],0)

            if s_dict[s[start]] == 0:
                del s_dict[s[start]]

            start+=1
            if p_dict == s_dict:
                ans.append(start)
        
        return ans

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
