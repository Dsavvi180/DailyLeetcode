class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        distanceToTarget = sorted([(target-x, index) for index, x in enumerate(position)], key=lambda tuple: tuple[0])
        
        for distance, index in distanceToTarget:
            timeToTarget = distance / speed[index]
            
            # If the car catches the fleet ahead, ignore it
            if stack and stack[-1] >= timeToTarget:
                continue
                
            # Otherwise, it forms a new fleet! Just append the time.
            stack.append(timeToTarget)
            
        return len(stack)