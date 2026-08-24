class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        memo = {}

        def dfs(cumSum: int, position: int) -> bool:
            if cumSum == target:
                return True
            if position >= n or cumSum > target:
                return False

            state = (position, cumSum)
            if state in memo:
                return memo[state]

            # Option 1: Pick nums[position]
            # Option 2: Skip nums[position]
            memo[state] = dfs(cumSum + nums[position], position + 1) or dfs(cumSum, position + 1)
            return memo[state]

        return dfs(0, 0)