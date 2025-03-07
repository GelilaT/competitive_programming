class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def generatePrime(right):
            isprime = [True for _ in range(right + 1)]
            isprime[0] = isprime[1] = False
            i = 2
            while i * i <= right:
                if isprime[i]:
                    j = i * i
                    while j <= right:
                        isprime[j] = False
                        j += i
                i += 1
            return isprime

        is_prime = generatePrime(right)
        primes = []
        for i in range(left, len(is_prime)):
            if is_prime[i]:
                primes.append(i)

        if len(primes) >= 2:
            diff = primes[1] - primes[0] 
            ans = [diff,[primes[0],primes[1]]]
            for i in range(2, len(primes)):
                dif = primes[i] - primes[i - 1]
                if dif < ans[0]:
                    ans[0] = dif
                    ans[1] = [primes[i - 1], primes[i]]
            return ans[1]
        else:
            return [-1,-1]
            