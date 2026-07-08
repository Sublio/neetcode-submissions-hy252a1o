class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #1. Go through each cell on the grid to see of this cell is "0" or "1"
        visited = set()
        res = 0
        def dfs(grid, r,c,visited):
            ROWS, COLS = len(grid), len(grid[0])
            if (min(r,c) <0 or r ==ROWS or c==COLS or (r,c) in visited):
                return 
            if grid[r][c] == "1":
                visited.add((r,c))
                grid[r][c] = "0" #2. Mark visited cell to not visit again 
            elif grid[r][c] == "0":
                return  #3. Kinda found the edge of the island thus we return 1 from function.
            dfs(grid, r+1, c, visited)
            dfs(grid, r-1, c, visited)
            dfs(grid, r, c+1, visited)
            dfs(grid, r, c-1, visited)
            return 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # 2. Call our dfs function
                    dfs(grid, i,j,visited)
                    res +=1
        return res
        