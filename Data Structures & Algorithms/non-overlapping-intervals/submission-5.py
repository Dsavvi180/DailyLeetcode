class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        print(intervals)
        n = len(intervals)
        nonOverlapping = [intervals[0]]
        i = 1
        x = 0
        while i < n and x< i:
            prev = nonOverlapping[x]
            current = intervals[i]
            if current[0]< prev[1]:
                print("yes", current)
                i+=1
                continue
            i+=1 
            x+=1
            print("appending current: ", current)
            nonOverlapping.append(current)
        print(nonOverlapping)
        return n-len(nonOverlapping)



        
        