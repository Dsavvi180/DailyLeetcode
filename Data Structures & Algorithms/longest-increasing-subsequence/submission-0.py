class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        
        def dfs(prev_index):
            if prev_index in memo:
                return memo[prev_index]
            
            maxLen = 1
            for i in range(prev_index+1, n):
                if nums[i] > nums[prev_index]:
                    res = dfs(i)
                    maxLen = max(maxLen, res+1)
            memo[prev_index] = maxLen

            return maxLen
        
        return max(dfs(i) for i in range(n))


                    





        