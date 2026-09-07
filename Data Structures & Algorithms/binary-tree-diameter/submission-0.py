# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # input: tree
        # output: length of longest path between 2 nodes (edges)
        # constraint: -100 <= node.val 
        # approach: Max height?
        # max height or its child + left + right node
        def find_height(node):
            nonlocal mx
            if node is None:
                return 0
            
            left = find_height(node.left)
            right = find_height(node.right)
            
            path = left + right + 1
            height = 1 + max(left, right)
            mx = max(mx, path, height)
            return height
        
        mx = -1
        h = find_height(root)

        return mx - 1


