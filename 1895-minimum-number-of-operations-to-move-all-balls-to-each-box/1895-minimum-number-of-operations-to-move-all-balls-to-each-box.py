class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ones = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                ones.append(i)

        ans = []
        for i in range(len(boxes)):
            n = 0
            for j in range(len(ones)):
                n += abs(ones[j] - i)

            ans.append(n)

        return ans