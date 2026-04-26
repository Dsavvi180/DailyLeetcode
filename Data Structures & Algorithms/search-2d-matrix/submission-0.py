class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattenedMatrix = []
        for i in matrix:
            flattenedMatrix.extend(i)
        def binarySearch(nums, target):
            left,right = 0,len(nums)-1
            while left<=right:
                pivot = (left+right)//2
                if nums[pivot] == target:
                    return True
                elif nums[pivot]<target:
                    left = pivot+1
                else:
                    right = pivot-1
            return False
        return binarySearch(flattenedMatrix,target)
        