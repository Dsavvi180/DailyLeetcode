import math
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.cache = [-1] * (n)

        def step(position):

            if position >= n:
                return 0

            if self.cache[position] == -1:
                self.cache[position] = min(step(position+1), step(position+2)) + cost[position]
            
            return self.cache[position]
        
        step(0)
        step(1)
        print(self.cache)
        return min(self.cache[0], self.cache[1])
        