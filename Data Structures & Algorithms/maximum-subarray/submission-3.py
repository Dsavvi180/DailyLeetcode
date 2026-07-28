class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        curSum = nums[0]
        maxSum = nums[0]
        for num in nums[1:]:
            if curSum +num < num:
                curSum = num
            else:
                curSum +=num
            maxSum = max(curSum, maxSum)

        return maxSum