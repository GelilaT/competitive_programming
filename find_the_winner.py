class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=list(range(n))
        idx=0
        while len(arr) > 1:
            idx=(idx+k-1) % len(arr)
            arr.pop(idx)
        return arr[0]+1
