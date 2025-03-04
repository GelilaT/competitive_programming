class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        summ = 0
        max_exp = 16
        while max_exp >= 0:

            temp = 3 ** max_exp
            if summ + temp < n:
                summ += temp
            
            elif summ + temp == n:
                return True

            max_exp -= 1

        return False
