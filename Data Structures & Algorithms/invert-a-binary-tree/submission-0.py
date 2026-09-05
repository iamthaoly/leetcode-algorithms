# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert(self, curr):
        if curr is None:
            return
        
        temp = curr.left
        curr.left = curr.right
        curr.right = temp
        
        self.invert(curr.left)
        self.invert(curr.right)
        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root
        