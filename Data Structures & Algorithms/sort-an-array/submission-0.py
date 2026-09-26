class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(nums):
            n = len(nums)
            split = n//2
            
            if len(nums) > 1:
                left = mergeSort(nums[:split])
                right = mergeSort(nums[split:])
                merged = []
                pointLeft, pointRight = 0, 0
                while pointLeft<len(left) and pointRight<len(right):
                    if left[pointLeft]<right[pointRight]:
                        merged.append(left[pointLeft])
                        pointLeft+=1
                    else:
                        merged.append(right[pointRight])
                        pointRight+=1
                merged.extend(left[pointLeft:])
                merged.extend(right[pointRight:])
                return merged
            else:
                return nums

        return mergeSort(nums)