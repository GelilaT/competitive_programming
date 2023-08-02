class Solution:
    def racecar(self, target: int) -> int:

        queue = deque()
        queue.append((0, 1, 0))
        visited = set((0, 1))
        while queue:
            for i in range(len(queue)):
                pos, speed, ans = queue.popleft()
                if pos == target:
                    return ans
                for j in range(2):
                    if j == 0:
                        if (pos + speed, speed * 2) not in visited:
                            queue.append((pos + speed, speed * 2, ans + 1))
                            visited.add((pos + speed, speed * 2))
                    
                    elif j == 1:
                        if speed > 0:
                            newspeed = -1
                            
                        else:
                            newspeed = 1
                        
                        if (pos, newspeed) not in visited:
                            queue.append((pos, newspeed, ans + 1))
                            visited.add((pos, newspeed))