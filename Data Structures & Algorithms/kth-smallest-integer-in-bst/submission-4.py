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
                left = dfs(node.left)
                if left:
                    return left

            count += 1
            if count > k:
                return None
            if count == k:
                val = node.val
                return val

            if node.right:
                right = dfs(node.right)
                if right:
                    return right

            return None
        count = 0
        val = 0
        dfs(root)
        return val