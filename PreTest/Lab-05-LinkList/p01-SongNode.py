"""

วันหนึ่งนายที่มาก่อน y แต่หลัง w อยากลองทดสอบเสียงจึงไล่คีย์โน้ต โด เร มี ฟา ซอน ลา ที แต่เขาไม่ชอบที่ร้องซ้ำคีย์เดิม และมีคีย์อยู่ในหัวใจ แต่คนอื่นในจักรวาลมักจะให้คีย์ที่ไม่ถูกใจเขา เขาจึงอยากวอนขอให้โปรแกรมเมอร์ระดับจักรวาลช่วยเขียนโปรแกรมนี้ขึ้นมา โดยการทำงานมีดังนี้

อินพุทแรก จะรับคีย์โน้ตโดยสามารถซ้ำกันได้ และคั่นด้วยช่องว่าง
อินพุทที่สอง จะรับ serie of operation และจะคั่นด้วยคอมม่า โดยมี 3 รูปแบบดังนี้

D(Delete) : ให้ทำการลบตัวหลังสุดของ LinkedList
R(Rename) : ให้เปลี่ยนคีย์โน้ตตัวหลังสุดของ LinkedList ตามที่ป้อนมา เช่น R mi แปลว่า เปลี่ยนจาก … เป็น mi
A(Add) : ให้เพิ่มคีย์โน้ตตามที่ป้อมมา เช่น A mi แปลว่า เพิ่มโน้ต mi ต่อท้าย LinkedList

ด้วยการรับมาในครั้งเดียว แบ่ง อินพุททั้ง 2 ด้วยเครื่องหมาย / 
ให้แสดงผล LinkedList 3 ครั้ง โดยมีรูปแบบเป็นไปตาม Test Case
ก่อนจะทำตาม operation ต่างๆที่ป้อนมา
หลังจากทำตาม operation
LinkedList ที่ไม่มีข้อมูลซ้ำกัน


สามารถเพิ่มโค้ดในบรรทัดที่เขียนว่า #CODE HERE หรือเพิ่ม method ในคลาส LinkedList ได้

****Note****

-หากมี Error เกิดขึ้นในระหว่างที่ทำ operation ให้แสดงคำว่า Error!!! ทันที
-ถ้า LinkedList ว่าง ให้แสดงคำว่า LinkedList is empty!


*******ห้ามใช้ List! ให้ใช้ class Node ในการทำ Linked List เท่านั้น*********



"""

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None

    def appendHead(self, value):
        node = Node(value, self.head)
        self.head = node

    def appendLast(self, value):
        if self.head == None:
            self.appendHead(value)
            return
        p = Node(value)
        t = self.head
        while t.next != None:
            t = t.next
        t.next = p

    def removeLast(self):
        if self.head == None:
            print("Error!!!")
            return
        if self.head.next == None:
            self.head = None
            return
        p = self.head
        while p.next.next != None:
            p = p.next
        p.next = None

    def rename(self, newName):
        if self.head == None:
            print("Error!!!")
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.value = newName

    def printList(self):
        if self.head is None:
            print("Linklist is empty!")
            return
        p = self.head
        while p != None:
            if p.next == None:
                print(p.value)
            else:
                print(p.value, end=" -> ")
            p = p.next

    def printListWithNoDuplicate(self):
        seen = set()
        if self.head == None:
            print("Linklist is empty!")
            return
        p = self.head
        result = []
        while p != None:
            if p.value not in seen:
                seen.add(p.value)
                result.append(p.value)
            p = p.next
        if result:
            print(" -> ".join(result))
        else:
            print("LinkedList is empty!")

def convertToLinkList(ls):
    listSong = ls[0].strip().split(" ")
    operations = ls[1].strip().split(", ")
    
    myLinkList = LinkList()
    
    for note in listSong:
        myLinkList.appendLast(note)
    
    myLinkList.printList()
    
    for op in operations:
        op = op.strip().split(" ")
        if op[0] == "D":
            myLinkList.removeLast()
        elif op[0] == "R":
            myLinkList.rename(op[1])
        elif op[0] == "A":
            myLinkList.appendLast(op[1])
        
    return myLinkList

print("*** My Favourite Keynote ***")
string = input("Enter Input / List of operation : ").strip().split("/")
myLinkList = convertToLinkList(string)
myLinkList.printList()
myLinkList.printListWithNoDuplicate()
