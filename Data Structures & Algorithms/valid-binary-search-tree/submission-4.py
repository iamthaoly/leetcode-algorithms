# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, cur, arr) -> bool: 
        if cur is None:
            return True
        
        if not self.check(cur.left, arr):
            return False
        
        if (len(arr) == 0) or cur.val > arr[-1]:
            arr += [cur.val]
        else:
            return False

        if not self.check(cur.right, arr):
            return False

        return True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, [])
        