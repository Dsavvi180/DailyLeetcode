class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if nums[0]>=target:
            return 1
        
        minLen = math.inf
        left, right = 0,1
        
        currentSum = nums[left] + nums[right]

        while left <= right:
            if currentSum >= target:
                minLen = min(minLen, right-left+1)
                currentSum -= nums[left]
                left+=1
            elif currentSum < target:
                if right < len(nums)-1:
                   right += 1
                   currentSum += nums[right]
                else:
                    break

        return minLen if minLen < math.inf else 0



            