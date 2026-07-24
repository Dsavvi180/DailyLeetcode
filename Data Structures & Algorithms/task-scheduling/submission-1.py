import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = deque([])
        frequencyMap = {}

        for task in tasks:
            if task not in frequencyMap:
                frequencyMap[task] = 1
            else:
                frequencyMap[task] += 1
        nextTask = [(-frequency, task) for task, frequency in frequencyMap.items()]
        heapq.heapify(nextTask)

        time = 0
        while nextTask or cooldown:
            if cooldown and cooldown[0][0]<=time:
                heapq.heappush(nextTask, cooldown.popleft()[1])
            
            if nextTask:
                nextFreq, nextTsk = heapq.heappop(nextTask)
                if nextFreq+1<0:
                   cooldown.append((time+n+1, (nextFreq+1, nextTsk)))
            
            else:
                time = cooldown[0][0]-1
            time +=1
        
        return time



        





        