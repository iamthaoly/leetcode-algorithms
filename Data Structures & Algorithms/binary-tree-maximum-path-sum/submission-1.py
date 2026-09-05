# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_max(self, cur, max_sum) -> (int, int):
        if cur is None or cur.val is None:
            return (0, max_sum)
        l, msl = self.find_max(cur.left, max_sum)
        r, msr = self.find_max(cur.right, max_sum)

        max_sum = max(msl, msr, cur.val, cur.val + l, cur.val + r, cur.val + l + r)

        return (max(cur.val, cur.val + l, cur.val + r), max_sum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # A brute force solution is that, we check the sum of the path of every
        # two nodes, which leads to O(n^2) time complexity
        max_sum = -1000
        _, res = self.find_max(root, max_sum)

        return res
