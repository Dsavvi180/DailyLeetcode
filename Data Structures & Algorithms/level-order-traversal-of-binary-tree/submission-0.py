# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        output = [[root.val]]
        currentLevel = [root]
        
        while currentLevel:
            nextLevel = []
            nextLevelVals = []
            for node in currentLevel:
                if not node: continue
                nextLevel.append(node.left)
                nextLevel.append(node.right)
                if node.left:
                   nextLevelVals.append(node.left.val)
                if node.right:
                   nextLevelVals.append(node.right.val)
            if nextLevelVals:
                output.append(nextLevelVals)
            currentLevel = nextLevel
        return output





        