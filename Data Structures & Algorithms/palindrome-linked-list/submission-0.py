# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        node = head
        while node:
            arr.append(node)
            node = node.next

        for i in range(len(arr) // 2):
            if arr[i].val != arr[len(arr) - 1 - i].val:
                return False
        return True