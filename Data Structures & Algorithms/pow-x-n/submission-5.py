class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == float(1):
            return 1
        elif x == -float(1):
            return float(1) if n %2 == 0 else -float(1)
        isNegative = False
        if n<0:
            n*=-1
            isNegative = True
        cumSum = x
        if x == float(2):
            cumSum = 1 << n
        else:
            for i in range(n-1):
                cumSum*=x

        return 1/cumSum if isNegative else cumSum
        