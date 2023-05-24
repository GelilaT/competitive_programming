class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        if "0000" in deadends:
            return -1
        def neighbours(lock):
            res = []
            for i in range(4):
                second = lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:]
                first = lock[:i] + str((int(lock[i]) - 1) % 10) + lock[i+1:]
                res.append(first)
                res.append(second)
            return res
        
        deadends = set(deadends)
        queue = deque(["0000"])
        count = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return count
                res = neighbours(cur)
                for adj in res:
                    if adj not in deadends:
                        deadends.add(adj)
                        queue.append(adj)
            count += 1
        return -1