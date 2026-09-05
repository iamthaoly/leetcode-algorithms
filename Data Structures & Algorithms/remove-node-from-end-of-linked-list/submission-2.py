# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        i = 0
        while (i < n):
            fast = fast.next
            i += 1

        # if not fast: # not correct
        #     return None
        
        prev = slow
        while(fast):
            prev = slow
            slow = slow.next
            fast = fast.next

        # handle 1 element
        if slow == head:
            head = head.next
        else:
            prev.next = slow.next
        # slow = None
        return head

