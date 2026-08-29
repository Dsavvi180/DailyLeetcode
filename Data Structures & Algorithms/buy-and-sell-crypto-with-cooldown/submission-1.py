class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(holding, ith_day):

            if (holding, ith_day) in memo:
                return memo[(holding, ith_day)]

            if ith_day >= len(prices):
                return 0 

            if holding and ith_day == len(prices) -1: # cash in, return profits
               return prices[ith_day]
            
            maxProfit = 0
            if holding: # we can sell or continue holding
               sold = dfs(False, ith_day + 2) + prices[ith_day] # we sold so skip a day
               kept = dfs(holding, ith_day + 1) # we continue holding so move to next day
               maxProfit = max(sold, kept)
            else: # if not holding we consider buying or waiting
               buy = dfs(True, ith_day +1) - prices[ith_day] # buy, move to next day
               wait = dfs(holding, ith_day+1) # wait, move to next day
               maxProfit = max(buy, wait)
            
            memo[(holding, ith_day)] = maxProfit
            return maxProfit
        return dfs(False, 0)





            

        