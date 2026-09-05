# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        
        n = len(arr)
        res = cur = ListNode()
        mid = n // 2
        for i in range(mid + 1):
            cur.next = arr[i]
            cur = cur.next
            if n - 1 - i > (mid):
                cur.next = arr[n - 1 - i]
                cur = cur.next

        cur.next = None

    def reorderList2(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head
        while (cur):
            arr += [cur]
            cur = cur.next
        
        n = len(arr)
        print(n)
        res = cur = ListNode()
        for i in range(n // 2 + 1):
            cur.next = arr[i]
            cur = cur.next
            if n - 1 - i > (n // 2):
                cur.next = arr[n - 1 - i]
                cur = cur.next

        return res.next
