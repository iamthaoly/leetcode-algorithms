# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Solution 2: Iteration (optimized)
        n1, n2 = l1, l2
        rem = 0
        node = res = ListNode()
        # print(9 // 10)
        while n1 or n2 or rem:
            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0
            summ = (val1 + val2 + rem)
            digit = summ % 10
            rem = summ // 10
            node.next = ListNode(digit)
            n1, n2 = n1.next if n1 else None, n2.next if n2 else None
            node = node.next
        
        return res.next

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Solution 1: Iteration
        n1, n2 = l1, l2
        rem = 0
        node = res = ListNode()
        # print(9 // 10)
        while n1 or n2:
            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0
            summ = (val1 + val2 + rem)
            digit = summ % 10
            rem = summ // 10
            node.next = ListNode(digit)
            n1, n2 = n1.next if n1 else None, n2.next if n2 else None
            node = node.next
        
        while rem > 0:
            digit = rem % 10
            rem = rem // 10
            node.next = ListNode(digit)
        
        return res.next

