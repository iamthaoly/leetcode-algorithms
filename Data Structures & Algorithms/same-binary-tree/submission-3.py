# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorder(self, cur1, cur2) -> bool:
        if cur1 is None or cur2 is None:
            if cur1 == cur2:
                return True
            return False

        left_matched = self.postorder(cur1.left, cur2.left)
        right_matched = self.postorder(cur1.right, cur2.right)
        if (cur1.val == cur2.val and left_matched and right_matched):
            return True
        else:
            return False
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.postorder(p, q)