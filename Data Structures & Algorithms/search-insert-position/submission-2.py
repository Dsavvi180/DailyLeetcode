class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left < right:
            midpoint = int((left+right)/2)
            print("midpoint: ", midpoint)
            print("left: ", left)
            print("right: ", right)
           
    
            midval = nums[midpoint]
            print(nums[left:right+1])
            print(midval)
            if midval == target:
                return midpoint
            elif target < midval:
                right = midpoint-1
            else:
                left = midpoint+1
        
        if target >nums[left]:
            return left +1
        else:
            return max(left ,0)
    
  
