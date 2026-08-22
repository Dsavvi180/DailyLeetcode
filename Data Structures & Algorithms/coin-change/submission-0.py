class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        n = len(coins)
        memo = {}
        
        def dfs(remainder):
            if remainder == 0:
                return 0
            if remainder < 0:
                return
            if remainder in memo:
                return memo[remainder]
            
            minResult = math.inf
            for coin in coins:
                if coin <= remainder:
                    result = dfs(remainder - coin)
                    minResult = min(minResult, result+1)
            memo[remainder] = minResult

            return memo[remainder]

        ans = dfs(amount)
        return ans if ans != math.inf else -1

                

            


        
        