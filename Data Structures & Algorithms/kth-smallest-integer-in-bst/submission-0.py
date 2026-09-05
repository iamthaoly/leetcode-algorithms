# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    def inorder(self, cur, k) -> int:
        if cur == None:
            return None
        
        if self.count < k:
            res = self.inorder(cur.left, k)
            if res is not None:
                return res
        self.count += 1
        if k == self.count:
            return cur.val
        if self.count < k:
            res = self.inorder(cur.right, k)
            if res is not None:
                return res
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorder(root, k)