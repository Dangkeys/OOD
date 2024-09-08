class Node:
    def __init__(self,data,next=None,prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
class DoublyLinkedList:
    def __init__(self) -> None:
        self.header = Node(None)
        self.trailer = Node(None,prev=self.header)
        self.header.next = self.trailer
        self.size = 0
    def append(self,data):
        node = Node(data,next=self.trailer,prev=self.trailer.prev)
        self.trailer.prev.next = node
        self.trailer.prev = node
        self.size += 1
        return node
    def add_head(self,data):
        node = Node(data,next = self.header.next,prev = self.header)
        self.header.next.prev = node
        self.header.next = node
        self.size += 1
        return node
    def remove_head(self):
        if self.header.next == self.trailer:
            return None
        old_node = self.header.next
        self.header.next = old_node.next
        old_node.next.prev = self.header.next
        self.size -= 1
        return old_node
    
    def pop(self):
        if self.header.next == self.trailer:
            return None
        old_node = self.trailer.prev
        self.trailer.prev = old_node.prev
        old_node.prev.next = self.trailer
        return old_node
    def __str__(self) -> str:
        log = ''
        current_node = self.header.next
        while current_node != self.trailer:
            log += str(current_node.data) + ' <- '
            current_node = current_node.next
        return log.rstrip(' <- ') if log else 'Empty'
linkedList = DoublyLinkedList()
print(linkedList)
linkedList.pop()
print(linkedList)

linkedList.append(2)
print(linkedList)
linkedList.append(3)
print(linkedList)
linkedList.add_head(1)
print(linkedList)
linkedList.pop()
print(linkedList)
# linkedList.add_head(1)
# print(linkedList)
# linkedList.add_head(0)
# print(linkedList)
# linkedList.remove_head()
# print(linkedList)
# linkedList.remove_head()
# print(linkedList)