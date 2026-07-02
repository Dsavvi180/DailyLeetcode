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
        currentLevel = deque([root.left, root.right])
        rootLeft = root.left
        rootRight = root.right
        root.left = rootRight
        root.right = rootLeft
        while currentLevel:
            node = currentLevel.popleft()
            if node:
                nodeLeft = node.left 
                nodeRight = node.right
                node.left = nodeRight
                node.right = nodeLeft
                currentLevel.append(nodeRight)
                currentLevel.append(nodeLeft)
        return root
                


