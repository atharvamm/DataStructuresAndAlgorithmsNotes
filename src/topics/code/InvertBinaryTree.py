


from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        def recurse(node):
            if node is None:
                return None
            
            node.left,node.right = node.right,node.left
            recurse(node.left)
            recurse(node.right)
            
        
        recurse(root)
        return root


