class TimeMap:
    def __init__(self):
        self.store = {}

    def binarySearch(self, timestamp, timestamps):
        left, right = 0, len(timestamps)-1
        if timestamps[left]>timestamp:
            return None
        while left<=right:
            middle = (left+right)//2
            if timestamps[middle] == timestamp:
                return timestamps[middle]
            elif timestamps[middle]<timestamp:
                left = middle+1
            else:
                right = middle -1
        return timestamps[left-1]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[timestamp], {timestamp:value}]
        else:
            self.store[key][0].append(timestamp)
            self.store[key][1][timestamp] = value
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            timestamps, timeValuePairs = self.store.get(key)
            result = timeValuePairs.get(self.binarySearch(timestamp, timestamps))
        else:
            result = None
        return result if result else ""