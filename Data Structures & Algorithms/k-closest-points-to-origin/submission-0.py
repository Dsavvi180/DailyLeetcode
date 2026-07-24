import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            distance = math.sqrt(point[0]**2+point[1]**2)
            if len(maxHeap)<k:
                heapq.heappush(maxHeap,(-distance,point))
            elif distance<-maxHeap[0][0]:
                heapq.heappushpop(maxHeap, (-distance,point))
        return [y for x,y in maxHeap]
        