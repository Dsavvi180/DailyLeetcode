class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        n = len(nums)

        for i in range(n):
            remainder = -nums[i]
            left, right = i+1, n-1

            while left<right:
                if left == i:
                    left +=1
                if right ==i:
                    right -=1
                if nums[left] + nums[right] == remainder:
                    output.add(tuple(sorted((nums[i], nums[left], nums[right]))))
                    left+=1
                    right-=1
                elif nums[left] + nums[right] > remainder:
                    right -=1
                else:
                    left +=1
        return [[x,y,z] for x,y,z in output]

            
            


            
                
                