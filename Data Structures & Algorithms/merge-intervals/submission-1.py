class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        i = 0
        mergedIntervals = []
        while i < n:
            count = i+1

            while count<n and intervals[count][0] <= intervals[i][1]:
                intervals[i][0] = min(intervals[count][0], intervals[i][0])
                intervals[i][1] = max(intervals[count][1], intervals[i][1])
                count += 1

            mergedIntervals.append(intervals[i])
            i = count  
        return mergedIntervals