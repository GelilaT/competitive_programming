class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        count = [0] * len(A) 
        ans = [0] * len(A)
        for i in range(len(A)):
            count[A[i] - 1] += 1
            count[B[i] - 1] += 1

            for j in range(len(A)):
                if count[j] == 2:
                    ans[i] += 1

        return ans 