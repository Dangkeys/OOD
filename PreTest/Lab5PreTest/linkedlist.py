class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.header = Node(None)
        self.size = 0

    def add_head(self, data) -> Node:
        node = Node(data, self.header.next)
        self.header.next = node
        self.size += 1
        return node

    def append(self, data) -> Node:
        node = Node(data)
        current_node = self.header
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        self.size += 1
        return node

    def __str__(self) -> str:
        log = ''
        current_node = self.header.next
        while current_node:
            log += str(current_node.data) + ' <- '
            current_node = current_node.next
        return log.rstrip(' <- ') if log else 'LinkedList is empty!'

    def remove_head(self) -> Node:
        if self.size == 0:
            return None  # Return None if there's nothing to remove
        old_head = self.header.next
        self.header.next = old_head.next
        old_head.next = None
        self.size -= 1
        return old_head

    def pop(self) -> Node:
        if not self.header.next:
            return None  # Return None if there's nothing to pop
        current_node = self.header.next
        if not current_node.next:
            self.header.next = None
            self.size -= 1
            return current_node
        while current_node.next.next:
            current_node = current_node.next
        last_node = current_node.next
        current_node.next = None
        self.size -= 1
        return last_node

    def insert_at(self, data, i) -> Node:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        current_node = self.header
        for _ in range(i):
            current_node = current_node.next
        node = Node(data, current_node.next)
        current_node.next = node
        self.size += 1
        return node

    def remove_at(self, i) -> Node:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        current_node = self.header
        for _ in range(i):
            current_node = current_node.next
        remove_node = current_node.next
        current_node.next = remove_node.next
        remove_node.next = None
        self.size -= 1
        return remove_node

linkedList = LinkedList()
print(linkedList)
linkedList.append(2)
print(linkedList)
linkedList.add_head(1)
print(linkedList)
linkedList.append(3)
print(linkedList)
linkedList.remove_at(1)
print(linkedList)
linkedList.remove_at(0)
print(linkedList)
linkedList.insert_at(1, 0)
print(linkedList)
linkedList.insert_at(2, 1)
print(linkedList)
