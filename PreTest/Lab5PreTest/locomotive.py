class Node:
    def __init__(self,data, next = None) -> None:
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self) -> None:
        self.header = Node(None)
        self.size = 0
        
    def append(self,data):
        node = Node(data)
        current_node = self.header
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        self.size +=1
        return node
    
    def __str__(self) -> str:
        log = ''
        current_node = self.header.next
        while current_node:
            log += str(current_node.data) + ' <- '
            current_node = current_node.next
        return log.rstrip(' <- ') if log else 'LinkedList is empty!'
    def remove_head(self) -> Node:
        old_head = self.header.next
        self.header.next = old_head.next
        old_head.next = None
        
        return old_head
        
    def remove_head_and_append(self):
        node = self.remove_head()
        return self.append(node.data)
    def locomotive(self):
        while(self.header.next.data !='0' ):
            self.remove_head_and_append()
linkedList = LinkedList()
train = input("Enter Input : ").split()
for locomotive in train:
    linkedList.append(locomotive)   
print(f"Before : {linkedList}")
linkedList.locomotive()
print(f"After : {linkedList}")

