# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def inorder(self, cur, k) -> int:
        count = 0

        # use sub-function (def in def), and nonlocal
        # not need to refer self.count
        def travel(cur, k) -> int:
            nonlocal count
            if cur == None or count > k:
                return None
            

            # if it asks for a specific node value, add conditions
            # so it wont return None. Like below:
            res = travel(cur.left, k)
            if res is not None:
                return res

            count += 1
            if k == count:
                return cur.val


            res = travel(cur.right, k)
            if res is not None:
                return res
        
        return travel(cur, k)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorder(root, k)