class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        left, right = 0 ,1
        while left<right and right<len(prices):
            difference = prices[right] - prices[left]
            if difference>0:
                maxPrice = max(maxPrice, difference)
                right+=1
            else:
                right+=1
                left = right -1
                
        return maxPrice

        

        

        