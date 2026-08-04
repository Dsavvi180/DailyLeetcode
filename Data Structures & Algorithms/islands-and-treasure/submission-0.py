class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r,c, distance):
            if r< 0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == -1 :
                return
            if distance > grid[r][c]:
                return
            
            grid[r][c] = distance
            dfs(r,c+1,distance+1)
            dfs(r,c-1,distance+1)
            dfs(r+1,c,distance+1)
            dfs(r-1,c,distance+1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r,c,0)
            
        