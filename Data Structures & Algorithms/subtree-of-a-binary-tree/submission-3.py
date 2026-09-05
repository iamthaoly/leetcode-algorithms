# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def is_same_tree(self, cur1, cur2) -> bool:
        # post-order traversal
        if cur1 is None and cur2 is None:
            return True

        if (cur1 and cur2 and cur1.val == cur2.val and self.is_same_tree(cur1.left, cur2.left) and self.is_same_tree(cur1.right, cur2.right)):
            return True
        return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.is_same_tree(root, subRoot):
            return True
        if root.left and self.isSubtree(root.left, subRoot):
            return True
        if root.right and self.isSubtree(root.right, subRoot):
            return True
        return False


