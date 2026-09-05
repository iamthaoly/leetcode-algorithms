# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # input: 2 sorted linked list, 0 <= len(list) <= 100
        # output merged sorted list

        # max_value = -1000
        # node = None
        res = None
        if not (list1 or list2):
            return res

        cur1 = list1
        cur2 = list2
        cur1, cur2 = list1, list2
        if (not cur2) or (cur1 and (cur1.val < cur2.val)):
            res = cur1
            cur1 = cur1.next
        else:
            res = cur2
            cur2 = cur2.next
        prev = res

        while (cur1 or cur2):
            if (not cur2) or (cur1 and (cur1.val < cur2.val)):
                node = ListNode(cur1.val, None)
                cur1 = cur1.next
            else:
                node = ListNode(cur2.val, None)
                cur2 = cur2.next
            prev.next = node
            prev = node


        return res


