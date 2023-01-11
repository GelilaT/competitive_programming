class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1=num1[::-1]
        num2=num2[::-1]
        product=0
        for i in range(len(num1)):
            for j in range(len(num2)):
                n1=int(num1[i])*10**i
                n2=int(num2[j])*10**j
                product+=(n1*n2)
        return str(product)
