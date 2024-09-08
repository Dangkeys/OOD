""" 
ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้
1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
3. reverse     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่ท้ายไปจนหัวมีตัวอะไรบ้าง
4. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
5. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
6. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
7. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
8. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
9. size           คืนค่าเป็นขนาดของ Linked List
10. pop         นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range
11. insert       เป็นการนำ Item ไปแทรกใน Linked List ตามตำแหน่ง pos ไม่มีการคืนค่า

ถ้าน้องยังไม่ค่อยเข้าใจการทำงานของ insert ให้น้องลองกับ List บน Python ได้  เช่น
1.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(0,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]
2.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(999,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , 2 , 3 , "T" ]
3.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-2,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , "T" , 2 , 3 ]  
4.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-10,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]

โดยรูปแบบ Input มีดังนี้
1. append    ->  AP
2. addHead  ->  AH
3. search      ->  SE
4. index        ->   ID
5. size          ->   SI
6. pop          ->   PO
7. insert       ->   IS

โดยให้เพิ่มเติมจากส่วน #Code Here ของโปรแกรมต่อไปนี้ เพื่อให้สามารถแสดงผลได้ตามที่โจทย์กำหนด
********  ห้ามใช้ List ในการทำ Linked List เด็ดขาดถ้าหากพบจะถูกลดเป็น 0 คะแนน ********

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        #Code Here

    def addHead(self, item):
        #Code Here

    def insert(self, pos, item):
        #Code Here

    def search(self, item):
        #Code Here

    def index(self, item):
        #Code Here

    def size(self):
        #Code Here

    def pop(self, pos):
        #Code Here

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())


Enter Input : AP I,AP Love,AP KMITL,AP 2020
Linked List : I Love KMITL 2020 
Linked List Reverse : 2020 KMITL Love I 

Enter Input : PO -999,PO 999,PO 0,AP KMITL,PO 999,PO 0
Out of Range | Empty
Out of Range | Empty
Out of Range | Empty
Out of Range | KMITL 
Success | KMITL -> Empty
Linked List : Empty
Linked List Reverse : Empty

Enter Input : SI,AH 2020,SI,AH KMITL,SI,AH LOVE,SI,AH I,SI
Linked List size = 0 : Empty
Linked List size = 1 : 2020 
Linked List size = 2 : KMITL 2020 
Linked List size = 3 : LOVE KMITL 2020 
Linked List size = 4 : I LOVE KMITL 2020 
Linked List : I LOVE KMITL 2020 
Linked List Reverse : 2020 KMITL LOVE I


Enter Input : SI,IS 0 KMITL,SI,SE 0,SE KMITL,ID 0,ID KMITL,PO 0,SI,IS -999 CE,SI
Linked List size = 0 : Empty
Linked List size = 1 : KMITL 
Not Found 0 in KMITL 
Found KMITL in KMITL 
Index (0) = -1 : KMITL 
Index (KMITL) = 0 : KMITL 
Success | KMITL -> Empty
Linked List size = 0 : Empty
Linked List size = 1 : CE 
Linked List : CE 
Linked List Reverse : CE 

Enter Input : AP 0,AP 1,AP 2,AP 3,SI,IS -1 KMITL,SI,ID KMITL
Linked List size = 4 : 0 1 2 3 
Linked List size = 5 : 0 1 2 KMITL 3 
Index (KMITL) = 3 : 0 1 2 KMITL 3 
Linked List : 0 1 2 KMITL 3 
Linked List Reverse : 3 KMITL 2 1 0 


Enter Input : AP 0,AP 1,AP 2,AP 3,SI,IS 999 KMITL,SI
Linked List size = 4 : 0 1 2 3 
Linked List size = 5 : 0 1 2 3 KMITL 
Linked List : 0 1 2 3 KMITL 
Linked List Reverse : KMITL 3 2 1 0 


Enter Input : AH 3,AH 2,AH 1,AH 0,SI,IS -3 KMITL,SI
Linked List size = 4 : 0 1 2 3 
Linked List size = 5 : 0 KMITL 1 2 3 
Linked List : 0 KMITL 1 2 3 
Linked List Reverse : 3 2 1 KMITL 0 


Enter Input : AP 0,AP 1,AP 2,AP 3,SI,IS -999 KMITL,SI
Linked List size = 4 : 0 1 2 3 
Linked List size = 5 : KMITL 0 1 2 3 
Linked List : KMITL 0 1 2 3 
Linked List Reverse : 3 2 1 0 KMITL 

"""

class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.prev = None
        self.data = data

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __str__(self):
        if self.head == None:
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.head == None:
            return "Empty"
        cur, s = self.tail, str(self.tail.data) + " "
        while cur.prev != None:
            s += str(cur.prev.data) + " "
            cur = cur.prev
        return s

    def isEmpty(self):
        return self.head == None
    
    def append(self, data):
        p = Node(data)
        if self.isEmpty():
            self.head = self.tail = p
        else:
            self.tail.next = p
            p.prev = self.tail
            self.tail = p

    def addHead(self, data):
        p = Node(data)
        if self.isEmpty():
            self.head = self.tail = p
        else:
            self.head.prev = p
            p.next = self.head 
            self.head = p
    
    def search(self, data):
        if self.isEmpty():
            return 'Not FOund'
        cur = self.head
        while cur.next != None:
            if cur.data == data:
                return "Found"
            cur = cur.next
        return "Not Found"
    
    def index(self, data):
        if self.isEmpty():
            return -1
        i = 0
        cur = self.head
        while cur.next != None:
            if cur.data == data:
                return i
            cur = cur.next
        return -1
    
    def size(self):
        s = 0
        cur = self.head
        while cur != None:
            s+=1
            cur = cur.next
        return s

    def pop(self, pos):
        if pos < 0 or pos >= self.size():
            return "Out of Range"
        elif pos == 0:
            self.head = self.tail = None
            return "Success"
        elif pos == self.size()-1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            cur = self.head
            for _ in range(pos-1):
                cur = cur.next
            cur.next.next.prev = cur
            cur.next = cur.next.next
        return "Success"
    
    def insert(self, pos, item):
        p = Node(item)
        if self.isEmpty():
            self.addHead(item)
        elif pos >= self.size():
            self.append(item)
        elif pos < 0:
            pos = self.size() + pos
            if pos <= 0:
                self.addHead(item)
            else:
                cur = self.head
                for _ in range(pos-1):
                    cur = cur.next
                cur.next = p
                p.prev = cur
                cur.next.next.prev = p
                p.next = cur.next.next.prev
        else:
                cur = self.head
                for _ in range(pos-1):
                    cur = cur.next
                cur.next = p
                p.prev = cur
                cur.next.prev = p
                p.next = cur.next.prev

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    # print("Do ", i)
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())