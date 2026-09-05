# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = head
        a = []
        
        while(node):
            a += [node]
            node = node.next
        
        res = ListNode()
        node = res
        r = 0
        l = 0
        for i in range(len(a)):
            if i % 2 == 0:
                node.next = a[l]
                l += 1
            else:
                node.next = a[len(a) - 1 - r]
                r += 1
            node = node.next
        
        node.next = None
            


