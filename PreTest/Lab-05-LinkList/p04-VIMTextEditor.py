""" 
กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor

***** อธิบาย Input 5 แบบ *****

1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป

2.  L              :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

3.  R             :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

4.  B             :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

5.  D             :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร


Enter Input : I Apple,I Bird,I Cat
Apple Bird Cat | 

Enter Input : I Apple,I Bird,I Cat,L
Apple Bird | Cat 

Enter Input : I Apple,I Bird,I Cat,L,L
Apple | Bird Cat 

Enter Input : I Apple,I Bird,I Cat,L,L,L,L,L
| Apple Bird Cat 

Enter Input : I Apple,I Bird,I Cat,L,L,R
Apple Bird | Cat 

Enter Input : I Apple,I Bird,I Cat,L,L,R,B
Apple | Cat 

Enter Input : I Apple,I Bird,L,L,R,D,D
Apple | 

Enter Input : L,R,I ABC,I DE,L,I FGHI
ABC FGHI | DE 

Enter Input : I A,I B,L,L,R,D,D,L,L,R,I BCD,L,L,B,D,R,R,L,L
| BCD 

Enter Input : I I,I KMITL,L,L,R,I Love
I Love | KMITL 

Enter Input : I I,I KMITL,L,L,R,I Love,D,I DataStructure,L,L,R,L,R,B,I Hate
I Hate | DataStructure

"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return str(self.data)
        
class LinkList:
    def __init__(self, head=None):
        self.head = head
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def removeHead(self):
        if self.head is None:
            return
        self.head = self.head.next
        
    def removeTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        
    def removeNodeByIndex(self, i):
        if self.head is None:
            return
        if i == 0:
            self.head = self.head.next
            return
        temp = self.head
        count = 0
        while temp is not None:
            if count == i-1 and temp.next is not None:
                temp.next = temp.next.next
                return
            temp = temp.next
            count += 1
        
    def insertAfter(self, i, data):
        new_node = Node(data)
        temp = self.head 
        count = 0
        while temp is not None:
            if count == i: 
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            count += 1
            
    def insertBefore(self, i, data):
        if i == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        temp = self.head
        count = 0
        while temp is not None:
            if count == i-1:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            count += 1
            
    def searchIndexByData(self, data):
        temp = self.head
        count = 0
        while temp is not None:
            if temp.data == data:
                return count
            count += 1
            temp = temp.next
        return -1
    
    def searchDataByIndex(self, i):
        temp = self.head
        count = 0
        while temp is not None:
            if count == i:
                return temp.data
            count += 1
            temp = temp.next
        return None
    
    def sizeOfLinkList(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count
            
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
            
def create_vim_text_editor(str_input):
    head = Node("|")
    myLinkList = LinkList(head)
    
    for command in str_input:
        ops = command.strip().split(" ")
        cmd = ops[0]
        word = str(ops[1]) if len(ops) > 1 else None
        
        cursor_index = myLinkList.searchIndexByData("|")
        
        if cmd == "I":
            myLinkList.insertAfter(cursor_index, word)
            myLinkList.removeNodeByIndex(cursor_index)
            myLinkList.insertAfter(cursor_index, "|")
            
        elif cmd == "L":
            if cursor_index > 0:
                myLinkList.removeNodeByIndex(cursor_index)
                myLinkList.insertBefore(cursor_index-1, "|")
                
        elif cmd == "R":
            if cursor_index < myLinkList.sizeOfLinkList() - 1:
                myLinkList.removeNodeByIndex(cursor_index)
                myLinkList.insertAfter(cursor_index, "|")
                
        elif cmd == "B":
            if cursor_index > 0:
                myLinkList.removeNodeByIndex(cursor_index - 1)
                
        elif cmd == "D":
            if cursor_index < myLinkList.sizeOfLinkList() - 1:
                myLinkList.removeNodeByIndex(cursor_index + 1)
                
    myLinkList.display()

# Example usage
str_input = input("Enter Input : ").strip().split(",")
create_vim_text_editor(str_input)
