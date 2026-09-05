# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # PRACTICE
        buffer = ListNode(0, head)
        slow = fast = buffer
        
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = None
                
            if slow and fast and slow == fast:
                return True
        
        return False
