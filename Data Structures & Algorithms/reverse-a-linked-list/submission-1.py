# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # input: int[], 0 <= len(list) <= 1000, -1000 <= list[i] <= 1000
        # output: int[]
        if not head:
            return None
        prev = head
        cur = head.next
        head.next = None

        res = head
        while cur:
            temp = cur.next
            cur.next = prev
            if not temp:
                res = cur
            prev = cur
            cur = temp

        return res
            
