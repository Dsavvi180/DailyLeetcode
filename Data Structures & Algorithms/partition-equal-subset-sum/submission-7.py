class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        memo = {}
    
        if total%2 != 0:
            return False

        def dfs(cumSum, position):
          
            if (position, cumSum) in memo:
                return memo[(position, cumSum)]

            if cumSum == total/2:
                return True
            
            found = False
            for i in range(position+1, n):
                if cumSum + nums[i] <= total/2:
                    res = dfs(cumSum + nums[i], i)
                    if res:
                        found = True
            memo[(position, cumSum)] = found

            return memo[(position, cumSum)]

        return any([dfs(nums[i], i) for i in range(n)])
        