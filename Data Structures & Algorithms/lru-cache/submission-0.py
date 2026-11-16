class Node:

    def __init__(self, val: int, key: int):
        self.val = val
        self.key = key
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.hashmap = {}
        self.capacity = capacity

    def insert(self, node):
        prev = self.right.prev
        node.prev = prev
        node.next = self.right
        prev.next = node
        self.right.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(value,key)
        
        if key in self.hashmap:
            self.remove(self.hashmap[key])    
        self.hashmap[key] = newNode
        self.insert(newNode)
        if len(self.hashmap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]
