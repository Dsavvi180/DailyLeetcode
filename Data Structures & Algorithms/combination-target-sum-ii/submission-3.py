class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        
        def backtrack(index, path, total):
            # No duplicate checking needed here!
            if total == target:
                results.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                # Skip duplicates at the same recursive depth
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                # Early stopping: if the current number pushes us over, 
                # all subsequent (larger) numbers will too.
                if total + candidates[i] > target:
                    break
                    
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()
                
        backtrack(0, [], 0)
        return results