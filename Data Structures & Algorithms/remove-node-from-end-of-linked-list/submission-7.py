# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
