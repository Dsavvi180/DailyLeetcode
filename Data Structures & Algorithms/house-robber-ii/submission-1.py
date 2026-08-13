class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        cache1 = [-1] * n
        cache2 = [-1] * n
        nums1 = nums[:n-1][:]
        nums2 = nums[1:][:]
        
        def dfs(house,nums, cache):
            
            if house >= n-1:
                return 0

            if cache[house] == -1:
                cache[house] = max(nums[house] + dfs(house+2,nums, cache), dfs(house+1,nums, cache))
            
            return cache[house]
        
        return max(dfs(0,nums1, cache1), dfs(0, nums2, cache2))