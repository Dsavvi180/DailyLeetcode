class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(total, position):

            if total == target and position == len(nums):
                return 1
            elif position == len(nums) and total != target:
                return 0 

            if position > len(nums):
                return 0
            
            if (total, position) in memo:
                return memo[(total, position)]
       
            add = dfs(total-nums[position], position+1)
            subtract = dfs(total+nums[position], position+1)

            memo[(total, position)] = add + subtract

            return memo[(total, position)]

        return dfs(0,0)
        