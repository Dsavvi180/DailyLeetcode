class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i,j):
            print(i, j)
            if j>=len(t):
                print("match found")
                return 1

            if i>=len(s):
                print("end")
                return 0
            
            if (i,j) in memo:
                print(f"returning: ({i},{j}): {memo[(i,j)]}")
                return memo[(i,j)]
            
            x,y,z = 0,0,0
            if s[i] == t[j]:
                x = dfs(i+1, j+1)
                y = dfs(i+1, j)

            elif s[i] != t[j]:
                z = dfs(i+1,j)
     
            total = x+y+z
            memo[(i,j)] = total
            return total
        return dfs(0,0)

            
        