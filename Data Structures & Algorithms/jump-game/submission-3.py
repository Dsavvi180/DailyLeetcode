class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            jumps = nums[i]
            print(i+jumps)
            if i +jumps <goal:
                continue
            goal = i
        print(goal)
        if goal == 0:
            return True
        else:
            return False
            
            
