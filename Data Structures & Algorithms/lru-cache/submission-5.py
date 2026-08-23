class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


"""
cap 2

DLL
L 1 R

hmap
1 -> 10
2 -> 20
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.left = Node('left', 'left')
        self.right = Node('right', 'right')
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
        self.cur_cap = 0 

    def delete(self, node):
        cur_left = node.prev
        cur_right = node.next
        cur_left.next = cur_right
        cur_right.prev = cur_left
        self.cur_cap -= 1
        if node.key in self.hmap:
            del self.hmap[node.key]

    def add_to_front(self, node):
        right = self.right
        left = right.prev
        left.next = node
        node.prev = left
        node.next = right
        right.prev = node
        self.cur_cap += 1
        self.hmap[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1

        node = self.hmap[key]
        self.delete(node)
        self.add_to_front(node)
        return node.val      
        

    def put(self, key: int, value: int) -> None:
        # res = ""
        # head = self.left
        # while head:
        #     res += f" {head.key} "
        #     head=head.next

        # print(res)

        if key not in self.hmap:
            node = Node(key, value)
            self.add_to_front(node)
            self.hmap[key] = node

            if self.cur_cap > self.capacity:
                self.delete(self.left.next)
                # self.cur_cap -= 1
                # res = ""
                # head = self.left
                # while head:
                #     res += f" {head.key} "
                #     head=head.next

                # print(res)

        else:
            node = self.hmap[key]
            node.val = value
            self.delete(node)
            self.add_to_front(node)

        



        
