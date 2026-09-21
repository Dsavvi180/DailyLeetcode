import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
 
        timesMap = {}
        for u, v, t in times:
            if u in timesMap:
                timesMap[u].append([v, t])
            else:
                timesMap[u] = [[v, t]]

        # 1. Start with an empty set so we don't accidentally miscount
        visited = set()
        minHeap = [(0, k)]

        while minHeap:
            elapsedTime, currentNode = heapq.heappop(minHeap)
            
            # 2. THE CRUCIAL CHECK: If we already found a faster path to this node, ignore this slower one!
            if currentNode in visited:
                continue
                
            visited.add(currentNode)
            
            if len(visited) == n:
                return elapsedTime
                
            if currentNode not in timesMap:
                continue
                
            for v, t in timesMap[currentNode]:
                if v not in visited:
                   heapq.heappush(minHeap, (elapsedTime + t, v))
                   
        return -1

        
        