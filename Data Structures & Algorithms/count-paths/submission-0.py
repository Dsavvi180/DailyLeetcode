class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {} # stores the total number of unique paths from key (i,j) down to grid[m-1][n-1]

        def dfs(i,j):

            if (i,j) in memo:
                return memo[(i,j)]

            if i<0 or j<0 or i>=m or j>=n:
                return 0

            if i == m-1 and j == n-1:
                return 1
            
            down = dfs(i+1,j)
            right = dfs(i,j+1)

            memo[(i,j)] = down + right

            return down + right
        
        return dfs(0,0)


            

        