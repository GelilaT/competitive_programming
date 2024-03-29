class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
       
       stack = []
       count = 0
       for i in range(len(s)):
           if stack and stack[-1][0] == s[i]:
               stack[-1][1] += 1
               if stack[-1][1] == k:
                   stack.pop()

           else:
               stack.append([s[i], 1])

       return ''.join(key*value for key, value in stack)