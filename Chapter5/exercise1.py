# มีรถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่

# แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก

# โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้

# ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ

# เช่น 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6

# เป็น 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1 ( ให้ใช้ singly linked list)

class Node:
    def __init__(self, data, next = None) -> None:
        self.next = next
        self.data = data
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    def add_head(self, data):
        head = Node(data)
        if self.head == None:
            self.head = head
            return self.head
        head.next = self.head    
        self.head = head
        self.size += 1
        return self.head
    def remove_head(self):
        if self.head == None: return
        old_head = self.head
        self.head = self.head.next 
        self.size -= 1
        return old_head.data
    def append(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node
            self.size += 1
        return node.data
    def remove_head_and_append(self):
        return self.append(self.remove_head())
    
    def __str__(self) -> str:
        log = ""
        current_node = self.head
        while current_node != None and current_node.next != None:
            log += f"{str(current_node.data)} <- "
            current_node = current_node.next
        if current_node != None:
            log += str(current_node.data)
        return log if log else "Empty"
    
    def locomotive(self):
        while self.head.data != '0':
            self.remove_head_and_append()
            
print(" *** Locomotive ***")
linkedList = SinglyLinkedList()
train = input("Enter Input : ").split()
for locomotive in train:
    linkedList.append(locomotive)   
print(f"Before : {linkedList}")
linkedList.locomotive()
print(f"After : {linkedList}")
