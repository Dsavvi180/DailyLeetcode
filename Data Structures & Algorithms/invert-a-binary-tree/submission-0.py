# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        currentLevel = [root.left, root.right]
        nextLevel = []
        rootLeft = root.left
        rootRight = root.right
        root.left = rootRight
        root.right = rootLeft
        while currentLevel:
            for node in currentLevel:
                if node:
                    nodeLeft = node.left 
                    nodeRight = node.right
                    node.left = nodeRight
                    node.right = nodeLeft
                    nextLevel.append(nodeRight)
                    nextLevel.append(nodeLeft)
            currentLevel = nextLevel.copy()
            nextLevel.clear()
        return root
                


