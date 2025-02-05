class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2):
            return False

        if s1 == s2:
            return True

        count = 0
        idx = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                idx.append(i)
                
        if count == 2:
            if s1[idx[0]] == s2[idx[1]] and s1[idx[1]] == s2[idx[0]]:
                return True


        return False