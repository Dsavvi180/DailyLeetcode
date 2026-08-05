class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        visited = set()
        def dfs(r,c, group):
            inRange = lambda r,c : not (r<0 or c<0 or r>=ROWS or c>= COLS)
            visited.add((r,c))
            if inRange(r,c+1) and heights[r][c+1]>=heights[r][c] and (r,c+1) not in visited:
                dfs(r,c+1, group)
            if inRange(r,c-1) and heights[r][c-1]>=heights[r][c] and (r,c-1) not in visited:
                dfs(r, c-1, group)
            if inRange(r+1,c) and heights[r+1][c]>=heights[r][c] and (r+1,c) not in visited:
                dfs(r+1,c, group)
            if inRange(r-1,c) and heights[r-1][c]>=heights[r][c] and (r-1,c) not in visited:
                dfs(r-1,c, group)
            group.add((r,c))
            return
        pacific = set()
        atlantic = set()
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r,c, pacific)
                    visited.clear()
                if r == ROWS-1 or c == COLS-1:
                    dfs(r,c, atlantic)
                    visited.clear()
        results = []
        for p in pacific:
            if p in atlantic:
                results.append([p[0],p[1]])
            
        return results




        