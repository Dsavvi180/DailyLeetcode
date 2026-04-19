class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        setNums = set(nums)
        visitedSet = set()
        maxLen = 0
        # nums = sorted(nums)
        for i in range(n):
            if nums[i] in visitedSet:
                continue
            count = 1
            nextNum = nums[i]+1
            prevNum = nums[i] -1
            visitedSet.add(nums[i])
            while nextNum in setNums and not prevNum in setNums:
                visitedSet.add(nextNum)
                count += 1
                nextNum += 1 
            maxLen = max(count,maxLen)
            if maxLen == n:
                break
        return maxLen