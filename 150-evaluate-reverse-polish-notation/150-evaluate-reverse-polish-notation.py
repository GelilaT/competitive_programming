class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
          mystack=[]
          for char in tokens:
            if char=="+":
                mystack.append(mystack.pop()+mystack.pop())
            elif char=="-":
                first,second=mystack.pop(),mystack.pop()
                mystack.append(second-first)
            elif char=="*":
                mystack.append(mystack.pop()*mystack.pop())
            elif char=="/":
                first,second=mystack.pop(),mystack.pop()
                mystack.append(int(second/first))
            else:
                mystack.append(int(char))
          return mystack.pop()