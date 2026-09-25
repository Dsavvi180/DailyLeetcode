import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        minimumEffort = [[math.inf]*len(heights[0]) for _ in range(len(heights))]
        minimumEffort[0][0] = 0
        
        directions = [(1,0),(-1,0), (0,1), (0,-1)]

        minheap = [(0, (0,0))]
        
        while minheap:
            currentEffort, currentNode = heapq.heappop(minheap)
            r, c = currentNode
            minimumEffort[r][c] = min(minimumEffort[r][c], currentEffort)
            if r==rows-1 and c==cols-1:
                return currentEffort

            if currentEffort > minimumEffort[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    jumpEffort = abs(heights[r][c]-heights[nr][nc])
                    nextEffort = max(jumpEffort, currentEffort)

                    if nextEffort < minimumEffort[nr][nc]:
                        minimumEffort[nr][nc] = nextEffort
                        heapq.heappush(minheap, (nextEffort, (nr, nc)))
        return 0
             

            



        

            



        