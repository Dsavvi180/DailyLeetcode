class Solution:
    def withinTime(self, k, piles,h):
        totalTime = 0
        for pile in piles:
            totalTime += math.ceil(pile/k)
        return totalTime <=h

    def binarySearch(self,left,right,piles,h):

        while left<right:
            middle = (left+right)//2
            if self.withinTime(middle, piles,h):
                right = middle
            else:
                left = middle+1
        return right


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.binarySearch(1,max(piles),piles, h)



          

                
            

        