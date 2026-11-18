class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  # Dummy LRU boundary
        self.tail = Node()  # Dummy MRU boundary
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def add(self, node: Node) -> None:
        # Insert right before dummy tail (MRU)
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def evict(self) -> Node:
        # Remove the node right after dummy head (LRU)
        lru_node = self.head.next
        self.remove(lru_node)
        return lru_node

class LRUCache:
    def __init__(self, capacity: int):
        self.lru = DoublyLinkedList()
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.lru.remove(node)
        self.lru.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.lru.remove(node)
            self.lru.add(node)
        else:
            if len(self.cache) == self.capacity:
                evicted = self.lru.evict()
                del self.cache[evicted.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.lru.add(new_node)
