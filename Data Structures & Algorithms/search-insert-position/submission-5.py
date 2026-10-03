class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            midpoint = (left+right)//2
            midval = nums[midpoint]
           
            if midval == target:
                return midpoint
            elif target < midval:
                right = midpoint-1
            else:
                left = midpoint+1
        
        return left
    
  
