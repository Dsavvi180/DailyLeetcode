class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}
        
        def dfs(i, j):
            
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i

            if (i,j) in memo:
                return memo[(i,j)]

            operations = 0
            if word1[i] == word2[j]:
                operations = dfs(i+1,j+1)

            elif word1[i] != word2[j]:
                # insert, delete or replace
                insert = dfs(i, j+1) 
                delete = dfs(i+1, j)
                replace = dfs(i+1, j+1)

                operations = min(insert, delete, replace) + 1

            memo[(i,j)] = operations
            return memo[(i,j)]

        return dfs(0,0)


            


        