class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n-1
        maxArea = 0
        while left<right:
            width = right - left
            area = width*min(heights[left], heights[right])
            maxArea = max(maxArea, area)
            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right -=1
            else:
                left+=1
        return maxArea
        