class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        n = len(nums)

        for i in range(n):
            # 1. Skip duplicate 'i' values to prevent duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 2. Optimization: If the smallest number is > 0, they can never sum to 0
            if nums[i] > 0:
                break

            remainder = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                # 3. Redundant 'left == i' checks removed
                if nums[left] + nums[right] == remainder:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                    # Skip duplicate 'left' values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                elif nums[left] + nums[right] > remainder:
                    right -= 1
                else:
                    left += 1
                    
        return output
            
            


            
                
                