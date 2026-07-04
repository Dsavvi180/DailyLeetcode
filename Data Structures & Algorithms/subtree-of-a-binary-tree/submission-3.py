# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def matchSubtree(node, subRoot):
            queue = deque([(node.left, subRoot.left),(node.right,subRoot.right)])
            while queue:
                original, subNode = queue.popleft()
                if original and subNode:
                    print("original.val :", original.val)
                    print("subNode.val :", subNode.val)
                    if original.val == subNode.val:
                        queue.append((original.left, subNode.left))
                        queue.append((original.right, subNode.right))
                    else:
                        return False
                elif original and not subNode or not original and subNode:
                    print("returning false")
                    return False
            return True

        def dfs(node):
            if node:
                if node.val == subRoot.val:
                    if matchSubtree(node,subRoot):
                        print("matched")
                        return True
                    else:
                        left = dfs(node.left)
                        right = dfs(node.right)
                        return right or left
                left = dfs(node.left)
                right = dfs(node.right)
                return right or left
            return False
        result = dfs(root)
        return result
    
        