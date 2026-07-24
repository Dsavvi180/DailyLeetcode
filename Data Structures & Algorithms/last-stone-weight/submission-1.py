import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            x, y = abs(heapq.heappop(stones)), abs(heapq.heappop(stones))
            if x < y:
                heapq.heappush(stones, x-y)
            elif y<x:
                heapq.heappush(stones, y-x)
        return -stones[0] if stones else 0




        