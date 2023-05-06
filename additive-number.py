class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        path = []
        res = False
        def backtrack(idx):
            nonlocal res
            if res:
                return True
            if idx >= len(num):
                res = len(path) >= 3
                return 
            if len(path) > 1:
                prev = str(path[-1] + path[-2])
                if prev == num[idx: idx + len(prev)]:
                    path.append(int(prev))
                    backtrack(idx + len(prev))
                    path.pop()
                return
            if num[idx] == "0":
                path.append(0)
                backtrack(idx + 1)
                path.pop()
                return
            for end in range(idx, len(num)): 
                path.append(int(num[idx:end+1]))
                backtrack(end+1)
                path.pop()
        
        backtrack(0)
        return res