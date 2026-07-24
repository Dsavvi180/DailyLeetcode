import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        # min heap of k largest numbers in array
        for num in nums:
            if len(minHeap)<k:
                heapq.heappush(minHeap, num)
            elif num>minHeap[0]:
                heapq.heappushpop(minHeap, num)
       
        return minHeap[0]



        