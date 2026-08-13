class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache = [-1] * (n+1)
        
        def step(position):

            if position == n:
                return 1
            if position > n:
                return 0

            if self.cache[position] == -1:
                self.cache[position] = step(position+1) + step(position+2)
           
            return self.cache[position]
        
        step(0)

        return self.cache[0]

            

        


        