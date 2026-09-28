class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redCount, whiteCount, blueCount = 0,0,0

        for color in nums:
            if color == 0:
                redCount += 1
            elif color == 1:
                whiteCount += 1
            else:
                blueCount += 1

        nums.clear()
        nums.extend([0 for i in range(redCount)])
        nums.extend([1 for i in range(whiteCount)])
        nums.extend([2 for i in range(blueCount)])


               
