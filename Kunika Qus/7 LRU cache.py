from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed key to the end of the OrderedDict to mark it as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value if the key is already present
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # Add the new key-value pair
            if len(self.cache) >= self.capacity:
                # Remove the least recently used item (first item in OrderedDict)
                self.cache.popitem(last=False)
            self.cache[key] = value

    def print_cache(self) -> None:
        print(list(self.cache.items()))

# Example usage:
cache = LRUCache(2)  # Capacity is 2

cache.put(1, 1)
cache.put(2, 2)
cache.print_cache()  # Output: [(1, 1), (2, 2)]

print(cache.get(1))  # Output: 1
cache.print_cache()  # Output: [(2, 2), (1, 1)]

cache.put(3, 3)      # Evicts key 2 because capacity is reached
cache.print_cache()  # Output: [(1, 1), (3, 3)]

print(cache.get(2))  # Output: -1 (not found)


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key to node
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node: Node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # Remove from the head
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    def print_cache(self):
        current = self.head.next
        cache_contents = []
        while current != self.tail:
            cache_contents.append((current.key, current.value))
            current = current.next
        print(cache_contents)

# Example usage:
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.print_cache()  # Output: [(1, 1), (2, 2)]

print(cache.get(1))  # Output: 1
cache.print_cache()  # Output: [(2, 2), (1, 1)]

cache.put(3, 3)  # Evicts key 2
cache.print_cache()  # Output: [(1, 1), (3, 3)]

print(cache.get(2))  # Output: -1 (not found)


