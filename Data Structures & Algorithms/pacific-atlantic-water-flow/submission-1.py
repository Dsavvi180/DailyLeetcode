class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        visited = set()
        def dfs(r, c, group):
            inRange = lambda r, c : not (r<0 or c<0 or r>=ROWS or c>= COLS)
            
            # The group set now acts as our visited tracker!
            group.add((r, c)) 
            
            # Check if neighbor is valid, higher/equal, AND not already in this ocean's group
            if inRange(r, c+1) and heights[r][c+1] >= heights[r][c] and (r, c+1) not in group:
                dfs(r, c+1, group)
            if inRange(r, c-1) and heights[r][c-1] >= heights[r][c] and (r, c-1) not in group:
                dfs(r, c-1, group)
            if inRange(r+1, c) and heights[r+1][c] >= heights[r][c] and (r+1, c) not in group:
                dfs(r+1, c, group)
            if inRange(r-1, c) and heights[r-1][c] >= heights[r][c] and (r-1, c) not in group:
                dfs(r-1, c, group)

        pacific = set()
        atlantic = set()

        for r in range(ROWS):
            for c in range(COLS):
                # Pacific border check
                if (r == 0 or c == 0) and (r, c) not in pacific:
                    dfs(r, c, pacific)
                    
                # Atlantic border check
                if (r == ROWS-1 or c == COLS-1) and (r, c) not in atlantic:
                    dfs(r, c, atlantic)
                results = []
        for p in pacific:
            if p in atlantic:
                results.append([p[0],p[1]])
            
        return results




        