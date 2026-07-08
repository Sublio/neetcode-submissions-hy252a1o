class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        island_lengths = []
        res = 0
        def dfs(grid, r,c,visited):
            ROWS, COLS = len(grid), len(grid[0])
            count = 0
            
            if (min(r,c) <0 or r ==ROWS or c==COLS or (r,c) in visited):
                return 0
            if grid[r][c] == 1:
                visited.add((r,c))
                grid[r][c] = 0 #2. Mark visited cell to not visit again 
                count +=1
            elif grid[r][c] == 0:
                return 0 #3. Kinda found the edge of the island thus we return 1 from function.
            count += dfs(grid, r+1, c, visited)
            count += dfs(grid, r-1, c, visited)
            count += dfs(grid, r, c+1, visited)
            count += dfs(grid, r, c-1, visited)
            return count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # 2. Call our dfs function
                    island_lengths.append(dfs(grid, i,j,visited))
                    res = 0 # Need to nullify res after call otherwise it's going to be prev_res += new_res
        return max(island_lengths) if island_lengths else 0
        