class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n=len(s)
        my_dict={}
        stack=[]
        checker=set()

        for i in range(n):
            my_dict[s[i]]=i

        for i in range(n):
            if s[i] not in checker:
                while stack and stack[-1] > s[i] and i < my_dict[stack[-1]]:
                    checker.remove(stack[-1])
                    stack.pop()
                stack.append(s[i])
                checker.add(s[i])
            
        return ('').join(stack)
