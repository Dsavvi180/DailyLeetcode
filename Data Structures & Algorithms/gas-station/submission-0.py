class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            gasTank = gas[i]
            stationsTravelled = 0
            j = i
            circuitComplete = True
            while stationsTravelled < n:
                stationCost = cost[j]
                if gasTank >= stationCost:
                    gasTank -= stationCost
                    j = (j+1) % n
                    gasTank  += gas[j]
                    stationsTravelled += 1
                else:
                    circuitComplete = False
                    break
            if circuitComplete:
                return i
        return -1

            




        