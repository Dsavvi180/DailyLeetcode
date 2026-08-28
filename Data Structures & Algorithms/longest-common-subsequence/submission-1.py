class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        rows = len(text1)
        cols = len(text2)

        memo = {}

        def dfs(i,j):

            if (i,j) in memo:
                return memo[(i,j)]

            if i<0 or j<0 or i>=rows or j>=cols:
                return 0

            if i == rows - 1 and j == cols - 1:
                if text1[i] == text2[j]:
                    return 1
                else:
                    return 0

            diag = None
            down = None
            right = None

            if text1[i] == text2[j]:
                diag = dfs(i+1,j+1) + 1
                
            else:
                down = dfs(i+1, j)
                right = dfs(i, j+1)

            memo[(i,j)] = diag if diag else max(down,right)

            return memo[(i,j)]

        return dfs(0,0)

            
        