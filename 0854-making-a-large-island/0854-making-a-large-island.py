class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        directions = ((0,1), (1,0), (-1, 0), (0, -1))
        n = len(grid)
        group = 1
        sizes = dict()

        def color(i, j, group):
            grid[i][j] = group
            sizes[group] += 1
            for d in directions:
                _i, _j = i+d[0], j+d[1]
                if 0 <= _i<n and 0 <= _j<n and grid[_i][_j] == 1:
                    color(_i, _j, group)


        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    group += 1
                    sizes[group] = 0
                    color(i, j, group)


        if len(sizes) == 0:
            return 1
        

        visited = [1, 1, 1, 1]
        max_size = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    size = 1
                    visited[0], visited[1], visited[2], visited[3] = 1, 1, 1, 1
                    for k, d in enumerate(directions):
                        _i, _j = i+d[0], j+d[1]
                        if 0<=_i<n and 0<=_j<n:
                            group = grid[_i][_j] 
                            if group != 0 and group not in visited:
                                visited[k] = group
                                size += sizes[group]
                    max_size = max(size, max_size)

        return max(max_size, max(sizes.values()))


                    
        