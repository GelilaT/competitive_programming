class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=""
        x=str(x)
        for j in range(len(x)-1,-1,-1):
            num+=x[j]
        if num==x:
            return True
        else:
            return False
