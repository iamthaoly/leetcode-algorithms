# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        i = 0
        res = None
        def travel(preorder, inorder) -> TreeNode:
            nonlocal i, res
            if len(inorder) == 0:
                return None
            # if len(inorder) == 1:
            #     i += 1
            #     return TreeNode(inorder[0])

            root_val = preorder[i]
            root_index = inorder.index(root_val)

            cur = TreeNode(root_val)
            if i == 0:
                res = cur
            
            i += 1
            # if len(inorder) == 1:

            l = inorder[0:root_index]
            r = inorder[root_index+1::]

            cur.left = travel(preorder, l)
            cur.right = travel(preorder, r)
            return cur

        travel(preorder, inorder)
        return res