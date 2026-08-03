"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        nodeSet = {}
        nextQueue = deque([node])
        visited = set([])
        while nextQueue:
            currentNode = nextQueue.popleft()
            visited.add(currentNode.val)
            nodeCopy = Node(val = currentNode.val, neighbors = [])
            nodeSet[nodeCopy.val] = nodeCopy
            for neighbor in currentNode.neighbors:
                if neighbor.val not in visited:
                    nextQueue.append(neighbor)
                    visited.add(neighbor.val)
        nextQueue = deque([node])
        visited = set([])
    
        while nextQueue:
            currentNode = nextQueue.popleft()
            visited.add(currentNode.val)
            for neighbor in currentNode.neighbors:
                nodeSet[currentNode.val].neighbors.append(nodeSet[neighbor.val])
                if neighbor.val not in visited:
                    nextQueue.append(neighbor)
                    visited.add(neighbor.val)
        return nodeSet[node.val]

        
        

            
            
            
        

        