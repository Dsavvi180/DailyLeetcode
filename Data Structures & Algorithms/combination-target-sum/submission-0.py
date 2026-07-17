class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(pathSum, path, start):
            if pathSum == target:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                num = nums[i]
                if pathSum + num <= target:
                    path.append(num)
                    pathSum += num
                    backtrack(pathSum, path, i)
                    path.pop()
                    pathSum -= num
        
        backtrack(0, [], 0)
        return res

        