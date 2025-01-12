class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2:
            return False

        lock = []
        unlock = []
        for i, par in enumerate(s):
            if locked[i] == '0':
                unlock.append(i)

            elif par == '(':
                lock.append(i)

            elif par == ')':
                if lock:
                    lock.pop()
                elif unlock:
                    unlock.pop()
                else:
                    return False
        
        while unlock and lock and lock[-1] < unlock[-1]:
            unlock.pop()
            lock.pop()

        if lock:
            return False

        return True
                
        