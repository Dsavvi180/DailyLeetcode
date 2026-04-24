class MinStack:
    class Node:
        def __init__(self, val, prev=None):
            self.val = val
            self.prev = prev
    def __init__(self):
        self.stack = []
        self.min = None
        
    def push(self, val: int) -> None:
        newNode = self.Node(val)
        if not self.min:
            newNode.prev = None
            self.min = newNode
        elif val < self.min.val:
            newNode.prev = self.min
            self.min = newNode
        
        self.stack.append(newNode)

    def pop(self) -> None:
        element = self.stack.pop()
        if self.min and element == self.min:
            self.min = element.prev
        return element.val

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.min.val
        
