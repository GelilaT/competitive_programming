class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        new = abs(n)
        def changer(x,new):

            if x == 0:
                return 0   

            elif new == 0:
                return 1

            result = changer(x, new // 2)
            result = result * result

            if new % 2:
                return result * x

            return result

        result = changer(x, new)
        if new != n:
            return 1 / result

        return result