class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s= []
        i = 0
        for x in pushed:
            s.append(x)
            while s and s[-1] == popped[i]:
                s.pop()
                i+= 1
        return not s