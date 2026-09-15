class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for num in range(n+1):
            numOnes = 0
            for i in range(num+1):
                numOnes += 1 if num & (1 << i) != 0 else 0
            output.append(numOnes)
        return output

                
        