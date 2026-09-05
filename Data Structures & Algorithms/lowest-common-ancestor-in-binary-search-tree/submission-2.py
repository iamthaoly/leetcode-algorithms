# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find(self, cur, p, q) -> TreeNode:
        if (p <= cur.val <= q):
            return cur
        elif (p < q < cur.val):
            return self.find(cur.left, p, q)
        else:
            return self.find(cur.right, p, q)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        return self.find(root, p.val, q.val)