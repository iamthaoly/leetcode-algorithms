# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # Solution 2: BFS (optimized)
        if not root:
            return []
        
        q = deque([root])
        tree = []
        while q:
            size = len(q)
            level = [0] * size
            for i in range(size):
                node = q.popleft()
                if len(tree) % 2 != 0:
                    level[size - 1 - i] = node.val
                else:
                    level[i] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # if len(tree) % 2 != 0:
            #     level.reverse()
            tree.append(level)
        return tree