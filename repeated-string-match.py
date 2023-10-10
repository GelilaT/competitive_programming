class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        n = len(b)
        lps = [0] * n
        char = set()
        new_a = a + a[0]
        for i in range(1, len(new_a)):
            char.add(new_a[i - 1: i + 1])

        for i in range(1, len(b)):
            if b[i - 1: i + 1] not in char:
                return -1

        i, j = 0, 1
        while j < len(b):

            if b[i] == b[j]:
                lps[j] = i + 1
                i += 1 
                j += 1

            else:
                if i == 0:
                    j += 1
                else:
                    i = lps[i - 1]
        
        a_i, b_i = 0, 0
        count = 1
        while a_i < len(a) and b_i < len(b):

            if a[a_i] == b[b_i]:
                a_i += 1
                b_i += 1
            
            elif b_i == 0:
                a_i += 1

            else:
                b_i = lps[b_i - 1]

            if b_i == len(b):
                return count

            if a_i >= len(a):
                a_i = a_i % len(a)
                count += 1

            if count > len(b):
                break

        return -1