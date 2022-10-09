class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = ""
        lenn=len(s)
        for i in range(lenn):
         if (s[i] == '('):
            stack.append(i)
         elif (s[i] == ')'):
            word= s[stack[-1]:i + 1]
            s= s[:stack[-1]] + word[::-1] + s[i + 1:]
            del stack[-1]
 
        for i in range(lenn):
         if (s[i] != ')' and s[i] != '('):
            res += (s[i])
        return res 