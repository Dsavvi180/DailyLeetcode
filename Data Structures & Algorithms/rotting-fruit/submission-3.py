from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        nextInline = deque()
        numFreshFruits = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    nextInline.append((r,c))
                if grid[r][c] == 1:
                    numFreshFruits += 1
        
        # EARLY EXIT: If there are no fresh fruits, it takes 0 time.
        if numFreshFruits == 0:
            return 0
            
        time = 0
        queueLength = len(nextInline)
        
        while nextInline:
            r, c = nextInline.popleft()
            neighbors = [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]
            
            for x, y in neighbors:
                if x < 0 or y < 0 or x >= ROWS or y >= COLS or grid[x][y] != 1:
                    continue
                numFreshFruits -= 1
                grid[x][y] = 2
                nextInline.append((x, y))
                
            queueLength -= 1
            
            if queueLength == 0:
                time += 1
                queueLength = len(nextInline)
                
        return time - 1 if numFreshFruits == 0 else -1



        
        