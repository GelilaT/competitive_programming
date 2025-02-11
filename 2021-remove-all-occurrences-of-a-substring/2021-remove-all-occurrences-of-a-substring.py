class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        n = len(s)
        m = len(part)
        stack = []
        i = 0
        while i < n:
            stack.append(s[i])
            if len(stack) >= m and "".join(stack[len(stack) - m:]) == part:  
                del stack[-m:]
           
            i += 1

        return ("").join(stack)