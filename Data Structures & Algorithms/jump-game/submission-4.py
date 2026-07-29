class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            jumps = nums[i]
            if i +jumps <goal:
                continue
            goal = i
        if goal == 0:
            return True
        else:
            return False
            
            
