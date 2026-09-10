# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal count, val
            if node.left:
                dfs(node.left)
            count += 1
            if count == k:
                val = node.val
                # return node.val
            if node.right:
                dfs(node.right)
        count = 0
        val = 0
        dfs(root)
        return val