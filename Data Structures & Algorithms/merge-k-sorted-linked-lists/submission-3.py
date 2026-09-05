# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # PRACTICE MODE
        # HEAP
        # Forget heap syntax
        # add to list, instead of pushing to heap -> Wrong
        res = cur = ListNode()
        vals = []
        heapq.heapify(vals)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(vals, [lists[i].val, i])
                # vals.append([lists[i].val, i])

        # print(vals)
        while (vals):
            val, i = heapq.heappop(vals)
            cur.next = lists[i]
            cur = cur.next

            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(vals, [lists[i].val, i])

        return res.next

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # PRACTICE MODE
        # Brute force
        # Time: O(n * m)
        # Space: O(1)
        res = cur = ListNode()
        min_i = None
        count_empty = 0

        while(count_empty < len(lists)):
            count_empty = 0
            min_val = float('inf')

            for i in range(len(lists)):
                if lists[i] is None:
                    count_empty += 1
                if lists[i] and lists[i].val < min_val:
                    min_i = i
                    min_val = lists[i].val
            
            if min_val == float('inf'):
                break

            cur.next = lists[min_i]
            lists[min_i] = lists[min_i].next 
            cur = cur.next

        return res.next





