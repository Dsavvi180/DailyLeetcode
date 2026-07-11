# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: 
            return None
            
        split = inorder.index(preorder[0])
        leftSubtree = inorder[:split]
        rightSubtree = inorder[split+1:]
        
        root = TreeNode(preorder[0])
        
        # Pass the leftSubtree, and slice preorder from 1 to 1 + split
        root.left = self.buildTree(preorder[1 : split + 1], leftSubtree)
        
        # Pass the rightSubtree, and slice preorder from split + 1 to the end
        root.right = self.buildTree(preorder[split + 1 :], rightSubtree)
        
        return root