class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        stack=[]
        my_dict={}
        for i in range(n):
            if s[i] not in my_dict.keys():
                my_dict[s[i]]=i
                stack.append(1)
            else:
                index=my_dict[s[i]]
                j=i
                count=1
                while j > index:
                    j-=stack[-1]
                    count+=stack[-1]
                    stack.pop()

                stack.append(count)
        return stack
