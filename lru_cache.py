# Basic Implementation no pretty efficient
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # I used a dict instead of hash map
        self.body = {}
        # I used a list to have a control over the cache
        self.cache = list()

    def get(self, key: int) -> int:
        if key in self.body:
            self.cache.remove(key)
            self.cache.insert(0, key)
            return self.body[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.body:
            self.body[key] = value
            self.cache.remove(key)
            self.cache.insert(0, key)
        else:
            self.body[key] = value
            if len(self.cache) == self.capacity:
                last = self.cache[-1]
                self.cache.remove(self.cache[-1])
                del self.body[last]
            self.cache.insert(0, key)


# Best way with double linked list
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCacheBoosted:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, -1)
        self.tail = Node(0, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, value):
        node = self.cache.get(value, None)
        if node:
            self.move_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        node = self.cache.get(key, None)
        if node:
            node.value = value
            self.move_to_head(node)
        else:
            new_node = Node(key, value)
            if len(self.cache) == self.capacity:
                removed_tail = self.remove_tail_node()
                del self.cache[removed_tail.key]
            self.insert_to_head(new_node)
            self.cache[key] = new_node

    def insert_to_head(self, node):
        new_second_node = self.head.next
        new_second_node.prev = node

        node.next = new_second_node
        node.prev = self.head

        self.head.next = node

    def move_to_head(self, node):
        next_node = node.next
        previous_node = node.prev

        next_node.prev = previous_node
        previous_node.next = next_node

        self.insert_to_head(node)

    def remove_tail_node(self):
        node_to_delete = self.tail.prev
        new_tail = node_to_delete.prev

        self.tail.prev = new_tail
        new_tail.next = self.tail

        return node_to_delete


cache = LRUCacheBoosted(capacity=2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))


