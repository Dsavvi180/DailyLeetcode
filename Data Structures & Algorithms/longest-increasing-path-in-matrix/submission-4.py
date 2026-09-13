class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        memo = {}

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols:
                return 1

            if (i,j) in memo:
                return memo[(i,j)] 

            left, right, up, down = 0, 0, 0, 0
            inRange = lambda i,j: False if (i<0 or j<0 or i>=rows or j>=cols) else True
            # check left:
            if inRange(i,j-1) and matrix[i][j-1] > matrix[i][j]:
                left = dfs(i,j-1)
                
            # check right:
            if inRange(i,j+1) and matrix[i][j+1] > matrix[i][j]:
                right = dfs(i,j+1)
    
            # check up:
            if inRange(i-1,j) and matrix[i-1][j] > matrix[i][j]:
                up = dfs(i-1,j)
           
            # check down:
            if inRange(i+1,j) and matrix[i+1][j] > matrix[i][j]:
                down = dfs(i+1,j)

            longestPath = max(left, right, up, down) + 1 
            memo[(i,j)] = longestPath
            return memo[(i,j)]

        longestPath = 0
        for i in range(rows):
            for j in range(cols):
                longestPath = max(longestPath, dfs(i,j))

        return longestPath


        