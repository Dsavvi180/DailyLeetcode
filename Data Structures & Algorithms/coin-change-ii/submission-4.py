class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        memo = {}

        def dfs(total, position):

            if total > amount or position == len(coins):
                return 0

            if total == amount:
                return 1

            if (total, position) in memo:
                return memo[(total, position)]
    
            sameCoin = dfs(total+coins[position], position)
            nextCoin = dfs(total, position+1)
            
            memo[(total, position)] = sameCoin + nextCoin
            return sameCoin + nextCoin
        
        return sum(dfs(coins[i],i) for i in range(len(coins)))
