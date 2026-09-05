# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def postorder(cur: [TreeNode]) -> int:
            if cur is None:
                return 0

            l_height = postorder(cur.left) 
            r_height = postorder(cur.right)

            if l_height is None or r_height is None:
                return None

            l_height += 1
            r_height += 1

            if abs(l_height - r_height) > 1:
                return None
            
            return max(l_height, r_height)

        if postorder(root) is None:
            return False
        return True