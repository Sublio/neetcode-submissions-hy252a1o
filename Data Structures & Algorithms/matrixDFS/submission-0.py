class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, r,c, visit):
            rows, cols = len(grid), len(grid[0])
            if(min(r,c) < 0 or r >= rows or c>=cols or grid[r][c] == 1 or (r,c) in visit):
                return 0
            
            if r == rows-1 and c == cols-1:
                return 1

            visit.add((r,c))
            cnt = 0
            cnt += dfs(grid, r, c+1, visit)
            cnt += dfs(grid, r, c-1, visit)
            cnt += dfs(grid, r+1, c, visit)
            cnt += dfs(grid, r-1, c, visit)
            visit.remove((r,c))
            return cnt
        return dfs(grid, 0,0, set())
        