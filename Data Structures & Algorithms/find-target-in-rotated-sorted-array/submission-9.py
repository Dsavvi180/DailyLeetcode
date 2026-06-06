class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left<=right:
            middle = (left+right)//2
            if nums[middle]==target:
                return middle
            if nums[left]<=nums[middle]: #left half must be sorted
               # is the target in the left half?
                if nums[left]<= target < nums[middle]:
                   right = middle -1
                else: # go right half
                   left = middle +1
            else: # right half must be sorted
                if nums[middle]< target <= nums[right]:
                    left = middle +1
                else:
                    right = middle -1
        return -1

              

