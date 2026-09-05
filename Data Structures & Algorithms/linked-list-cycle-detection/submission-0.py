# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (not head):
            return False
        
        slow_p, fast_p = head, head
        while(slow_p):
            node = fast_p.next
            if (not node) or (not node.next): 
                return False
            
            fast_p = node.next # bug here
            if slow_p == fast_p:
                return True
            slow_p = slow_p.next
        
        return False