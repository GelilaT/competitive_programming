class Solution:
    def splitString(self, s: str) -> bool:
        self.arr=[]
        def split(prev,idx):
            if idx >= len(s):
                return True
            res = False
            for i in range(idx,len(s)):
                if prev - 1 == int(s[idx:i + 1]):
                    res = res or split(int(s[idx:i+1]),i + 1)
            
            return res
        
        res = False
        for i in range(len(s)-1):
            res = res or split(int(s[:i+1]),i+1)
        return res
