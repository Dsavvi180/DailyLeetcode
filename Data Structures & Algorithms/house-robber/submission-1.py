class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n
        
        def dfs(house):

            if house >= n:
                return 0

            if cache[house] == -1:
                cache[house] = max(nums[house]+dfs(house+2), dfs(house+1))

            return cache[house]

        dfs(0)

        return max(cache[0], cache[1] if len(cache)>1 else 0)