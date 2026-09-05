# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, cur, dep) -> int:
        if cur == None:
            return dep
        dep += 1

        dep_left = self.preorder(cur.left, dep)
        dep_right = self.preorder(cur.right, dep)
        dep = max(dep_left, dep_right)
        return dep

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.preorder(root, 0)
        