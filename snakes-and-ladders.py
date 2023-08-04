class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        dest = n * n

        def toRownCol(val):

            row = n - ((val - 1) // n) - 1
            col = (val - 1) % n 
            if (n - row) % 2 == 0: 
                col = n - col - 1

            return row, col

        queue = deque([(1, 0)])
        visited = set()

        while queue:

            pos, path = queue.popleft()
            if pos == dest:
                return path
            
            for step in range(1, 7):
                new_pos = pos + step
                if new_pos > dest:
                    break
                
                row, col = toRownCol(new_pos)
                if (row, col) not in visited:
                    visited.add((row, col))
                    if board[row][col] != -1:
                        new_pos = board[row][col]
                    
                    queue.append((new_pos, path + 1))

        return -1