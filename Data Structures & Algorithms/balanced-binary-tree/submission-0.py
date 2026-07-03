# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.unbalanced = False
        def dfs(node,depth):
            if node:
                depth +=1
                depthLeft = dfs(node.left, depth)
                depthRight = dfs(node.right, depth)
                if abs(depthLeft - depthRight)>1:
                    self.unbalanced = True
                return max(depthLeft, depthRight)
            return depth
        dfs(root,0)
        return not self.unbalanced

        