# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        fast = slow = head

        prev = slow
        while(fast and fast.next):
            fast = fast.next.next
            prev = slow
            slow = slow.next
        middle = slow
        if middle == head:
            return
        # split two lists
        prev.next = None

        # reverse list
        node = middle
        # print(createList(middle))
        prev = None
        while(node):
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        # print(createList(prev))
        # print(createList(head))
        # merge two list
        l1, l2 = head, prev
        res = ListNode()
        i = 0
        node = res

        while (l1 and l2):
            if (i % 2 == 0):
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
            i += 1
        node.next = l1 or l2
        # print(createList(res.next))
        




        