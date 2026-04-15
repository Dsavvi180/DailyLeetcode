class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {i:[] for i in range(1,len(nums)+1)} # frequency: values
        numStore = {}
        for num in nums:
            if num not in numStore:
                numStore[num] = 1
            else:
                numStore[num] +=1
        for num, value in numStore.items():
            count[value].append(num)
        values = []
        for freq, vals in reversed(count.items()):
            if len(vals)>0:
                values = values + vals
            if len(values) >=k:
                break
        return values