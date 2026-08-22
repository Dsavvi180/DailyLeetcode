class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [0] * n

        def dfs(start):
            if start == n:
                return True
            for i in range(start, n):
               
                if s[start:i+1] in wordDict:
                    res = False
                    if memo[i] != -1:
                       res = dfs(i+1)
                    if res:
                        memo[i] = True
                        return True
                    else:
                        memo[i] = -1
            return False
        res = dfs(0)
        return res
            
        