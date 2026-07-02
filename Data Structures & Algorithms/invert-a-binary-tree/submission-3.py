from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
            
        # Start the queue with just the root node
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # Swap the left and right children
            node.left, node.right = node.right, node.left
            
            # Add the children to the queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return root
