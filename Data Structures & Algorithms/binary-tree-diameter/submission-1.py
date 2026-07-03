# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, maxDepth):
            if node:
               maxDepth = maxDepth+1
            return max(dfs(node.left, maxDepth) if node else maxDepth, dfs(node.right, maxDepth) if node else maxDepth)
        
        singlePathCount = 0
        node = root
        while (not node.left and node.right) or (not node.right and node.left):
            if node.left:
                node = node.left
            else:
                node = node.right
            singlePathCount +=1
        
        leftTree, rightTree = node.left, node.right
        leftTreeMaxDepth, rightTreeMaxDepth = dfs(leftTree, 0), dfs(rightTree, 0)
        print("leftDepth: ", leftTreeMaxDepth)
        print("rightDepth: ", rightTreeMaxDepth)
        return max(leftTreeMaxDepth+rightTreeMaxDepth, leftTreeMaxDepth+singlePathCount,rightTreeMaxDepth+singlePathCount)
        
    

        