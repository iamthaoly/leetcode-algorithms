# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # PRACTICE
        # Solution 2: Two Pointers
        res = ListNode(0, head)
        l = r = res
        while n > 0:
            r = r.next
            n -= 1
        
        while l.next and r.next:
            l = l.next
            r = r.next

        l.next = l.next.next

        return res.next        
        


    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # PRACTICE
        # Solution 1: List
        cur = head
        arr = []
        while (cur):
            arr.append(cur)
            cur = cur.next

        i = len(arr) - n
        if i == 0:
            return head.next
        else:
            arr[i - 1].next = arr[i].next

        return head
