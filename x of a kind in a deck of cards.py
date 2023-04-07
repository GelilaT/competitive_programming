class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
       
        count = {}
        for i in range(len(deck)):
           count[deck[i]] = 1 + count.get(deck[i], 0)

        def GCD(a, b):
            if b == 0:
                return a
            else:
                return GCD(b, a % b)
        
        val = list(count.values())
        div = val[0]

        for i in range(len(val)):
            div = GCD(div, val[i])
        return div > 1
