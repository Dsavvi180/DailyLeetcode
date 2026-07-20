class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, currentPath):
            result.append(currentPath)
    

            for i in range(index, len(nums)):
                # if currentPath in results:
                #     continue
                currentPath.append(nums[i])
                backtrack(i+1, currentPath[:])
                currentPath.pop()
        backtrack(0,[])
        return result

        
        