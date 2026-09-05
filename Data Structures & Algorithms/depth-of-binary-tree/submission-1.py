# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorder(self, cur) -> int:
        if cur is None:
            return 0
        l = self.postorder(cur.left)
        r = self.postorder(cur.right)
        dep = 1 + max(l, r)
        return dep

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.postorder(root)
        