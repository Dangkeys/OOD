"""

เขียนโปรแกรมคลุกคำ (scramble) สร้าง singly linked list ของคำในจดหมาย scramble จดหมายโดยทำคล้ายตัด ไพ่และกรีดไพ่ ผู้รับจดหมาย descramble กรีดกลับและตัดกลับจนได้จดหมายฉบับเดิมที่อ่านได้(หากออกแบบดีๆ สามารถ scramble กี่ครั้งก็ได้ ขึ้นแรกให้ทำ ครั้งเดียวก่อน)  

***** รูปแบบ input *****

แบ่งเป็น 2 ฝั่ง ได้แก่ ฝั่งซ้าย (Linked List เริ่มต้น  ความยาวขั้นต่ำของ Linked List รับประกันว่าขั้นต่ำคือ 10)  |  ฝั่งขวา BottomUp กับ Riffle โดยการแทนด้วย B กับ R ซึ่งการรับ R กับ B สามารถสลับที่กันได้ เช่น   R 40,B 60  <->  B 60,R 40
1.  B   < percentage >  :  bottomUp ตัด ยกส่วนบน (lift) ออกตาม % input ที่รับเข้ามา นำส่วนล่างมาซ้อนทับส่วนบน
2.  R   < percentage >  :  riffleShuffle กรีด (จากด้านบน) lift ตาม % นำ node ของแต่ละลิสต์มาสลับกันทีละ node จากต้นลิสต์ ส่วนเกินนำมาต่อท้าย
***** ถ้าหากคิดเปอร์เซ็นของความยาว Linked List แล้วได้ทศนิยม ให้ปัดลงทั้งหมด *****
***** การแสดงผลมี Pattern เป็น   Bottomup  ->  Riffle  ->  Deriffle  -> Debottomup นะครับ

Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 62,B 23
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3
Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 50.000 % : 6 7 8 9 10 1 2 3 4 5
Riffle 50.000 % : 6 1 7 2 8 3 9 4 10 5
Deriffle 50.000 % : 6 7 8 9 10 1 2 3 4 5
Debottomup 50.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 23.000 % : 3 4 5 6 7 8 9 10 1 2
Riffle 62.000 % : 3 9 4 10 5 1 6 2 7 8
Deriffle 62.000 % : 3 4 5 6 7 8 9 10 1 2
Debottomup 23.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------

Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 16.98,B 68.42|R 26.9257,B 57
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3
Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 50.000 % : 6 7 8 9 10 1 2 3 4 5
Riffle 50.000 % : 6 1 7 2 8 3 9 4 10 5
Deriffle 50.000 % : 6 7 8 9 10 1 2 3 4 5
Debottomup 50.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 68.420 % : 7 8 9 10 1 2 3 4 5 6
Riffle 16.980 % : 7 8 9 10 1 2 3 4 5 6
Deriffle 16.980 % : 7 8 9 10 1 2 3 4 5 6
Debottomup 68.420 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 57.000 % : 6 7 8 9 10 1 2 3 4 5
Riffle 26.926 % : 6 8 7 9 10 1 2 3 4 5
Deriffle 26.926 % : 6 7 8 9 10 1 2 3 4 5
Debottomup 57.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------

Enter Input : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20/B 32.4367,R 49.5484863|B 89.4642,R 12.8962|R 11.546678,B 20.77867|R 40.56,B 93.7567
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 32.437 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4 5 6
Riffle 49.548 % : 7 16 8 17 9 18 10 19 11 20 12 1 13 2 14 3 15 4 5 6
Deriffle 49.548 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4 5 6
Debottomup 32.437 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 89.464 % : 18 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Riffle 12.896 % : 18 20 19 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Deriffle 12.896 % : 18 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Debottomup 89.464 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 20.779 % : 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
Riffle 11.547 % : 5 7 6 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
Deriffle 11.547 % : 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4
Debottomup 20.779 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
BottomUp 93.757 % : 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
Riffle 40.560 % : 19 7 20 8 1 9 2 10 3 11 4 12 5 13 6 14 15 16 17 18
Deriffle 40.560 % : 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
Debottomup 93.757 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
--------------------------------------------------

Enter Input : 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50|R 10,B 20|B 27,R 73
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 30.000 % : 4 5 6 7 8 9 10 1 2 3
Riffle 60.000 % : 4 10 5 1 6 2 7 3 8 9
Deriffle 60.000 % : 4 5 6 7 8 9 10 1 2 3
Debottomup 30.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 50.000 % : 6 7 8 9 10 1 2 3 4 5
Riffle 50.000 % : 6 1 7 2 8 3 9 4 10 5
Deriffle 50.000 % : 6 7 8 9 10 1 2 3 4 5
Debottomup 50.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 20.000 % : 3 4 5 6 7 8 9 10 1 2
Riffle 10.000 % : 3 4 5 6 7 8 9 10 1 2
Deriffle 10.000 % : 3 4 5 6 7 8 9 10 1 2
Debottomup 20.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10
BottomUp 27.000 % : 3 4 5 6 7 8 9 10 1 2
Riffle 73.000 % : 3 10 4 1 5 2 6 7 8 9
Deriffle 73.000 % : 3 4 5 6 7 8 9 10 1 2
Debottomup 27.000 % : 1 2 3 4 5 6 7 8 9 10
--------------------------------------------------

Enter Input : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30/B 89.4642,R 12.8962|R 11.546678,B 20.77867|R 40.56,B 93.7567|B 27.5495,R 73.1597
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
BottomUp 89.464 % : 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Riffle 12.896 % : 27 30 28 1 29 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Deriffle 12.896 % : 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Debottomup 89.464 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
BottomUp 20.779 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6
Riffle 11.547 % : 7 10 8 11 9 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6
Deriffle 11.547 % : 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6
Debottomup 20.779 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
BottomUp 93.757 % : 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
Riffle 40.560 % : 29 11 30 12 1 13 2 14 3 15 4 16 5 17 6 18 7 19 8 20 9 21 10 22 23 24 25 26 27 28
Deriffle 40.560 % : 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
Debottomup 93.757 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
BottomUp 27.549 % : 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8
Riffle 73.160 % : 9 30 10 1 11 2 12 3 13 4 14 5 15 6 16 7 17 8 18 19 20 21 22 23 24 25 26 27 28 29
Deriffle 73.160 % : 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8
Debottomup 27.549 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
--------------------------------------------------

Enter Input : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30/B 12.4642,R 89.8962|R 20.546678,B 11.77867|R 34.56,B 93.7567|B 79.5495,R 97.1597
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
BottomUp 12.464 % : 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3
Riffle 89.896 % : 4 30 5 1 6 2 7 3 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
Deriffle 89.896 % : 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3
Debottomup 12.464 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
BottomUp 11.779 % : 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3
Riffle 20.547 % : 4 10 5 11 6 12 7 13 8 14 9 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3
Deriffle 20.547 % : 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3
Debottomup 11.779 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
BottomUp 93.757 % : 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
Riffle 34.560 % : 29 9 30 10 1 11 2 12 3 13 4 14 5 15 6 16 7 17 8 18 19 20 21 22 23 24 25 26 27 28
Deriffle 34.560 % : 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
Debottomup 93.757 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
BottomUp 79.549 % : 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Riffle 97.160 % : 24 23 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
Deriffle 97.160 % : 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Debottomup 79.549 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
--------------------------------------------------

Enter Input : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30/B 64.2354,R 5.13542|R 98.4121,B 4.21952|R 12.345,B 67.89
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
BottomUp 64.235 % : 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Riffle 5.135 % : 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Deriffle 5.135 % : 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
Debottomup 64.235 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
BottomUp 4.220 % : 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1
Riffle 98.412 % : 2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
Deriffle 98.412 % : 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1
Debottomup 4.220 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
--------------------------------------------------
Start : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
BottomUp 67.890 % : 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
Riffle 12.345 % : 21 24 22 25 23 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
Deriffle 12.345 % : 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
Debottomup 67.890 % : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
--------------------------------------------------

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def insertBefore(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        count = 0
        while temp is not None:
            if count == index-1:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            count += 1
        
    def insertAfter(self, index, value):
        new_node = Node(value)
        temp = self.head
        count = 0
        while temp is not None:
            if count == index:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            count += 1
        
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
        
    def removeNodeByIndex(self, index):
        if self.head is None:
            return 
        if index == 0:
            self.head = self.head.next
            return 
        temp = self.head
        count = 0
        while temp is not None:
            if count == index-1 and temp.next is not None:
                temp.next = temp.next.next
                return
            temp = temp.next
            count += 1
            
    def removeNodeByValue(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.value == value:
                temp.next = temp.next.next
                return
            temp = temp.next
            
    def searchIndexByValue(self, data):
        temp = self.head
        count = 0
        while temp is not None:
            if temp.value == data:
                return count
            count += 1
            temp = temp.next
        return -1
    
    def searchValueByIndex(self, i):
        temp = self.head
        count = 0
        while temp is not None:
            if count == i:
                return temp.value
            count += 1
            temp = temp.next
        return None
        
def createLL(LL):
    myLinkList = LinkList()
    for i in range(0, len(LL)):
        myLinkList.append(LL[i])
    return myLinkList.head

def printLL(head):
    result = []
    while head is not None:
        result.append(head.value)
        head = head.next
    return " ".join(result)

def SIZE(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def normal_bottomup(myLL, b_point, size):
    current = myLL.head
    i = 0
    
    while i < b_point:
        myLL.append(current.value)
        myLL.removeHead()
        current = current.next
        i += 1
    
    return myLL.head
    
def normal_riffle(myLL, r_point, size):
    current = myLL.head
    storage = LinkList()
    i = 0

    while current is not None and i < size:
        if i >= r_point:
            storage.append(current.value)
            myLL.removeNodeByIndex(r_point)
        current = current.next
        i += 1
        
    current = myLL.head
    storage_current = storage.head
    current_size = SIZE(myLL.head)
    i = 0
    while storage_current is not None:
        if i < current_size:
            myLL.insertAfter(i, storage_current.value)
            current_size = SIZE(myLL.head)
            i += 2
        else:
            myLL.append(storage_current.value)
        storage_current = storage_current.next
    
    return myLL.head

def special_deriffle(myLL, r_point, size):
    storage = LinkList()
    current = myLL.head
    i = 0
    # print(f"size: {size}, r_point: {r_point}")
    
    if r_point > size // 2:
        while i < SIZE(myLL.head) and i <= size - r_point:
            storage_value = myLL.searchValueByIndex(i)
            storage.append(storage_value)
            myLL.removeNodeByIndex(i)
            current = current.next
            i += 1
        # print("deriffle storage part 1 :", printLL(storage.head))
        while current is not None:
            storage.append(current.value)
            myLL.removeNodeByIndex(i-1)
            current = current.next
        # print("deriffle storage part 2 :", printLL(storage.head))
    else:
        while i < SIZE(myLL.head) and i < r_point:
            storage_value = myLL.searchValueByIndex(i)
            storage.append(storage_value)
            myLL.removeNodeByIndex(i)
            i += 1
    
    storage_size = SIZE(storage.head)
    while storage_size > 0:
        interupt_value = storage.searchValueByIndex(storage_size-1)
        myLL.prepend(interupt_value)
        storage_size -= 1
    
    return myLL.head

def special_debottomup(myLL, b_point, size):
    move = size - b_point
    current = myLL.head
    i = 0
    
    while i < move:
        myLL.append(current.value)
        myLL.removeHead()
        current = current.next
        i += 1
    
    return myLL.head

def scarmble(head, b, r, size):
    bottomup_value = round(b, 3)
    riffle_value = round(r, 3)
    b_point = (bottomup_value * size) // 100
    r_point = (riffle_value * size) // 100
    
    myLL = LinkList()
    temp = head
    while temp is not None:
        myLL.append(temp.value)
        temp = temp.next
        
    nb_head = normal_bottomup(myLL, b_point, size)   
    print("BottomUp {:.3f} % : {}".format(bottomup_value, printLL(nb_head)))
    
    nr_head = normal_riffle(myLL, r_point, size)
    print("Riffle {:.3f} % : {}".format(riffle_value, printLL(nr_head)))
    
    dr_head = special_deriffle(myLL, r_point, size)
    print("Deriffle {:.3f} % : {}".format(riffle_value, printLL(dr_head)))
    
    db_head = special_debottomup(LinkList(dr_head), b_point, size)
    print("Debottomup {:.3f} % : {}".format(bottomup_value, printLL(db_head)))

inp1, inp2 = input('Enter Input : ').strip().split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    k = [j.split(' ') for j in k]
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][1]), float(k[1][1]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][1]), float(k[0][1]), SIZE(h))
    print('-' * 50)