class Solution:
    def interpret(self, command: str) -> str:
        new=""
        for i in range(len(command)):
            if command[i]=="(":
                if command[i+1]==")":
                    new+="o"
                elif command[i+1]=="a":
                    new+="al"
            elif command[i]=="G":
                new+="G"
        return new
