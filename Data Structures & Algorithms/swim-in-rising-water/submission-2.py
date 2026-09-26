import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        maxheights = [[math.inf]*len(grid[0]) for _ in range(len(grid))]
        maxheights[0][0] = grid[0][0]

        minheap = [(grid[0][0],0,0)]

        while minheap:
            currentMaxHeight, r, c = heapq.heappop(minheap)
        
            if r == rows-1 and c == cols -1:
                return maxheights[r][c]  

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0<=nr<rows and 0<=nc<cols:
                    newMaxHeight = max(currentMaxHeight, grid[nr][nc])

                    if newMaxHeight >= maxheights[nr][nc]:
                        continue

                    maxheights[nr][nc] = newMaxHeight
                    heapq.heappush(minheap, (newMaxHeight, nr, nc))
        
        return 0










        