class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(a, b):
            m, n = len(a), len(b) 
            if n < m:
                return False

            if b[:m] == a and b[n - m:] == a:
                return True

            else:
                return False

        ans = 0
        n = len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    ans += 1

        return ans