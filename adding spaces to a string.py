class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index=0
        output=[]
        for space in spaces:
            output.append(s[index:space])
            index=space
        output.append(s[space:])
        return " ".join(output)
