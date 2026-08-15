class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        grid = [[False]*n for i in range(n)]
        
        palindromeCount = 0
        # Base case: all substrings of length 1
        for i in range(n):
            grid[i][i] = True
            palindromeCount += 1

        # Base case: all substrings of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                grid[i][i+1] = True
                palindromeCount += 1
            

        # Induct on strings of length longer than 3
        for length in range(3, n+1):
            for i in range(n - length +1 ):
                left, right = i, i+length -1
                if grid[left+1][right-1] and s[left] == s[right]:
                    grid[left][right] = True
                    palindromeCount += 1
        
        return palindromeCount
                    



        