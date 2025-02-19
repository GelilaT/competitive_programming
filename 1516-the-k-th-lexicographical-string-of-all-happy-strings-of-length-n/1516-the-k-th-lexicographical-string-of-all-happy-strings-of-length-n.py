class Solution:
    def getHappyString(self, n: int, k: int) -> str:
       
        q = deque(["a", "b", "c"])
        res = []
        
        while q:
            s = q.popleft()
            if len(s) == n:
                res.append(s)
                continue
            for ch in "abc":
                if s[-1] != ch:
                    q.append(s + ch)
        
        return "" if k > len(res) else res[k - 1]