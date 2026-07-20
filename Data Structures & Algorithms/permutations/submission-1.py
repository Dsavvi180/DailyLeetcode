class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        visited = set()

        def backtrack(path):
            # Base case: we've used all numbers
            if len(path) == len(nums):
                results.append(path[:])
                return
            
            # For permutations, we always check every number
            for num in nums:
                if num not in visited:
                    path.append(num)
                    visited.add(num)
                    
                    backtrack(path) # No index needed!
                    
                    # Backtrack (undo the choice)
                    visited.remove(num)
                    path.pop()

        backtrack([])
        return results