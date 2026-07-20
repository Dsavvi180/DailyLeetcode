class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        visited = set()

        def backtrack(index,path):
            if len(path) == len(nums):
                results.append(path[:])
                return
            
            for i in range(0, len(nums)):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    backtrack(i+1, path)
                    visited.remove(nums[i])
                    path.pop()

        backtrack(0,[])
        return results

        