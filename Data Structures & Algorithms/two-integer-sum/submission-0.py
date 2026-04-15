class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in store:
                return [store[difference], i]
            if num not in store:
                store[num] = i
            

        