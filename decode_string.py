class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                sub=""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                stack.pop()
                k=""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append( int(k) * sub)
        if len(stack) == 1 and stack[-1].isdigit():
            return ""
        return ("").join(stack)
