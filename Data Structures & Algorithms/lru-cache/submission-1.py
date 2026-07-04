class Node:
    def __init__(self, key, value):
        self.k = key
        self.v = value
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):

        self.cap = capacity
        self.cache = {}
        self.left = Node(-1, -1)
        self.right = Node(-2, -2)

        self.left.nxt = self.right
        self.right.prev = self.left    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        res = node.v

        # left n1  node mru   right
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

        mru = self.right.prev
        mru.nxt = node
        node.prev = mru
        node.nxt = self.right
        self.right.prev = node

        node.nxt = self.right
        self.right.prev = node

        return res        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.v = value

            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
        else:
            node = Node(key, value)
            self.cache[key] = node

        mru = self.right.prev
        mru.nxt = node
        node.prev = mru
        node.nxt = self.right
        self.right.prev = node

        node.nxt = self.right
        self.right.prev = node

        if len(self.cache) > self.cap:
            lru = self.left.nxt
            lru.prev.nxt = lru.nxt
            lru.nxt.prev = lru.prev
            del self.cache[lru.k]




        
