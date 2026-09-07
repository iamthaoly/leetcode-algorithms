# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def count_height(node):
            if not node:
                return 0
            # if not node.left and node.right:
            #     return 1

            left = count_height(node.left)
            right = count_height(node.right)

            if left == None or right == None:
                return None

            if abs(left - right) <= 1:
                return 1 + max(left, right)
            return None

        if not root:
            return True
        
        return count_height(root) != None
