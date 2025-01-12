class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2:
            return False

        stack = []
        count = 0
        for i, par in enumerate(s):
            if par == "(" or locked[i] == '0':
                count += 1

            elif par == ")":
                count -= 1

            if count < 0:
                return False

        count = 0
        for par, lock in zip(reversed(s), reversed(locked)):
            if lock == '0' or par == ')':
                count += 1
            elif par == '(':
                count -= 1

            if count < 0:
                return False
        
        return True
                
