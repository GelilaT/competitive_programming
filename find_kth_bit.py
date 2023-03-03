class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(string):
            inverted=""
            for char in string:
                if char == "0":
                    inverted += "1"
                else:
                    inverted += "0"
            return inverted

        def compose(index):

            if index == 1:
                return "0"
            else:
                return compose(index - 1) + "1" + invert(compose(index - 1))[::-1]

        new=compose(n)
        return new[k-1]
