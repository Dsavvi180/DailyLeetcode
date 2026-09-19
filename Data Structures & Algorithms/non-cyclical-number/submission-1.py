class Solution:
    def isHappy(self, n: int) -> bool:

        def sumPow(n):
            return int(sum(math.pow(int(i),2) for i in str(n)))

        cache = set([n])
        
        while True:
            n = sumPow(n)
            if n == 1:
                return True
            elif n in cache:
                return False
            else:
                cache.add(n)


        