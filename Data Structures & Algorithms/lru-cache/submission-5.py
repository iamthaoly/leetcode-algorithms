class LRUCache:
    class Node:
        def __init__(self, val, next = None, prev = None):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.Node(-1) # buffer
        self.tail = self.Node(-1) # buffer
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # Helper
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # Get is also counted as operation
            # Re-add to make the node as recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val[1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = self.Node([key, value])
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.val[0]]

        
