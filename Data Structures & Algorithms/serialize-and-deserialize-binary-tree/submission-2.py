# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # left, r, right
        a = []
        # fix: change name to preorder
        def inorder(cur):
            nonlocal a
            if cur is None:
                return
            a.append(cur.val)
            if cur.left is None:
                a.append("N")
            inorder(cur.left)

            if cur.right is None:
                a.append("N")
            inorder(cur.right)
        inorder(root)
        
        i = 0
        s = ",".join(map(str, a))
        return s

        def decode() -> TreeNode:
            nonlocal a, i
            cur = TreeNode(a[i])
            i += 1
            if a[i] != "N":
                cur.left = decode()
            i += 1
            if a[i] != "N":
                cur.right = decode()
            
            return cur
        def print_tree(cur):
            if cur is None:
                return
            print(cur.val, end=" ")
            print_tree(cur.left)
            print_tree(cur.right)

        # res = decode()
        # print(a)
        # print_tree(res)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        split = data.split(",")
        print(split)
        a = []
        for x in split:
            if x == "N":
                a.append(x)
            elif x:
                a.append(int(x))
        i = 0
        def decode() -> TreeNode:
            nonlocal a, i
            if i == len(a):
                return None
            cur = TreeNode(a[i])
            i += 1
            if a[i] != "N":
                cur.left = decode()
            i += 1
            if a[i] != "N":
                cur.right = decode()
            return cur
        return decode()
        # return None
