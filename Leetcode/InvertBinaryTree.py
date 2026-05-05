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
            
        q = deque([root])
            
        while q:
            c = q.popleft()

            c.left, c.right = c.right, c.left

            if c.left:
                q.append(c.left)
            if c.right:
                q.append(c.right)

        return root