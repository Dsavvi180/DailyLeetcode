class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        self.area = 0
        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == 0:
                return
            grid[r][c] = 0
            self.area +=1
            dfs(r, c+1) # right
            dfs(r, c-1) # left
            dfs(r-1, c) # down
            dfs(r+1, c) # up

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
                maxArea = max(maxArea, self.area)
                self.area = 0
        return maxArea
        