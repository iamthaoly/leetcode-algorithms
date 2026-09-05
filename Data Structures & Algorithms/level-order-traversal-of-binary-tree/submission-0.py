# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder_travel(self,cur, arr, level) -> int[[int]]:
        if cur is None:
            return []

        while level > len(arr) - 1:
            arr += [[]]

        arr[level] += [cur.val]
        self.preorder_travel(cur.left, arr, level+1)
        self.preorder_travel(cur.right, arr, level+1)

        return arr
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 0 <= the number of nodes <= 1000
        # binary tree -> max height = ...
        # arr = [[]] * 1000 # warning: may not correct
        arr = [[]]
        return self.preorder_travel(root, arr, 0)
