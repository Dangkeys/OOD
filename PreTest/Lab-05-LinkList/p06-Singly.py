""" 
ให้เขียนคลาสของ Singly Linked List ซึ่งมีเมท็อดดังนี้
1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
3. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
4. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
5. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
6. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
7. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
8. size           คืนค่าเป็นขนาดของ Linked List
9. pop            นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range

โดยรูปแบบ Input มีดังนี้
1. append    ->  AP
2. addHead  ->  AH
3. search      ->  SE
4. index        ->   ID
5. size          ->   SI
6. pop          ->   PO

โดยให้เพิ่มเติมจากส่วน #Code Here ของโปรแกรมต่อไปนี้ เพื่อให้สามารถแสดงผลได้ตามที่โจทย์กำหนด
********  ห้ามใช้ List ในการทำ Linked List เด็ดขาดถ้าหากพบจะถูกลดเป็น 0 คะแนน ********

"""

class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data

        if next is None:
            self.next = None
        else:
            self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.s = 0
    
    def __str__(self):
        if self.head == None:
            return "Empty"
        else:
            cur, s = self.head, str(self.head.data) + " "
            while cur.next != None:
                s += str(cur.next.data)+" "
                cur = cur.next
            return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self, data):
        p = Node(data)

        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        
        self.s += 1
    
    def addHead(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            p.next = self.head
            self.head = p
        self.s += 1

    def search(self, data):
        t = self.head
        while t != None:
            if t.data == data:
                return "Found"
            t = t.next
        return "Not Found"

    def index(self, data):
        t = self.head
        i = 0
        while t != None:
            if t.data == data:
                return i
            t = t.next
            i+=1
        return -1

    def size(self):
        return self.s

    def pop(self, pos):
        if pos < 0 or self.head == None:
            return "Out of Range"
        
        if pos == 0:
            self.head = self.head.next
        
        crr = self.head
        for i in range(pos-1):
            if crr.next == None:
                return "Out of Range"
            crr = crr.next
        
        target = crr.next
        if target == None:
            return "Out of Range"
        crr.next = target.next
        return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        if L.size() == 0:
            post_fix = ' in Empty'
        else:
            post_fix = f' in {L}'
        print("{0} {1}{2}".format(L.search(i[3:]), i[3:], post_fix))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)