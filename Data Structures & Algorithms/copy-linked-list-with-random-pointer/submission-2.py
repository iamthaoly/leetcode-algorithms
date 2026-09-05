"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Solution 1: Use dict
        if not head:
            return None
            
        ll = {}
        h = head
        while head:
            ll[head] = ll.get(head, Node(head.val))
            if head.next not in ll:
                ll[head.next] = Node(head.next.val) if head.next else None
            if head.random not in ll:                
                ll[head.random] = Node(head.random.val) if head.random else None
            
            ll[head].next = ll[head.next]
            ll[head].random = ll[head.random]
            head = head.next

        return ll[h]


        # Input: Linked list nodes, .next and .random
        # Output: Head of the deep copy of that linked list
        # Constraint:
        # - Dont point to the original list
        # - .random can be null
        # - Node values are not unique
        # - Linked list can be null
        # Pattern: linked list node at i.

