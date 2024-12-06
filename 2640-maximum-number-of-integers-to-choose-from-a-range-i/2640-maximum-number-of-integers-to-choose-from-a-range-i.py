class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        running = 0
        maxLen = 0
        banned = set(banned)
        for i in range(1, n + 1):

            if i in banned:
                continue

            running += i
            if running > maxSum:
                break

            maxLen += 1  

        return maxLen

            


            

