class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result=[]
        new=""
        opened=False
        for line in source:
            index=0
            while index < len(line):
                char=line[index]
                if char=="/" and index+1 < len(line) and line[index+1]=="*" and not opened:
                    opened=True
                    index+=1
                elif char=="/" and index+1 < len(line) and line[index+1]=="/" and not opened:
                    break
                elif char=="*" and  index+1 < len(line) and line[index+1]=="/" and opened:
                    opened=False
                    index+=1
                elif not opened:
                    new+=char
                index+=1
            if new!="" and not opened:
                 result.append(new)
                 new=""  
        return result
Console
