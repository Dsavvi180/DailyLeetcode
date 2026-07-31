class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas)<sum(cost):
            return -1
        i  = 0
        total = 0
        result = 0
        while i <n:
            total += gas[i] - cost[i]
            if total< 0:
                total = 0
                result = i+1
            i+=1
        return result

            




        