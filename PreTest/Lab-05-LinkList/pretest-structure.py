class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return str(self.data)

class LinkList:
    def __init__(self, head=None):
        self.head = head
    
    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        
    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def removeHead(self):
        temp = self.head
        if temp is None:
            return
        self.head = temp.next
        
    def removeTail(self):
        temp = self.head
        if temp is None:
            return
        if temp.next is None:
            self.head = None
            return
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
            
linkList = LinkList()
linkList.append(12)
linkList.append(25)
linkList.append(36)
linkList.append(42)
linkList.append(54)
linkList.removeHead()
linkList.removeTail()
linkList.display()

        