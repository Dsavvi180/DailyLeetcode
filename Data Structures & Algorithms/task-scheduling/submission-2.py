from collections import Counter
from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = Counter(tasks)
        queue = deque()
        nextTasks = [(-count, task) for task, count in freqMap.items()]
        heapq.heapify(nextTasks)
        
        cycles = 0
        while nextTasks or queue:
            while queue and queue[0][0] <= cycles:
                heapq.heappush(nextTasks, queue.popleft()[1])
            if nextTasks:
                count, task = heapq.heappop(nextTasks)
                if count+1<0:
                   queue.append((cycles+n+1, (count+1, task)))
            cycles += 1
        return cycles
        



        