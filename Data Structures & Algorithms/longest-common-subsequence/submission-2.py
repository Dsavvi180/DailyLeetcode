class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        
        # Create a 2D grid initialized with zeros
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Fill the grid based on our rules
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match: diagonal + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # No match: max of left or up
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                    
        # The bottom-right cell contains the length of the LCS
        return dp[rows][cols]
        return dfs(0,0)

            
        