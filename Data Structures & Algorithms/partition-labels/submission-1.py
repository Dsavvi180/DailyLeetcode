from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        n = len(s)
        counts = []
        for i in range(n):
            lastIndex[s[i]] = i
        i = 0
        start = 0
        endPartition = lastIndex[s[start]]
        while i < n:
            if i> endPartition:
                counts.append(endPartition-start+1)
                start = i
                endPartition = lastIndex[s[start]]
            if lastIndex[s[i]] > endPartition:
                endPartition = lastIndex[s[i]]
            i+=1
        counts.append(endPartition-start+1)
        return counts






        







        