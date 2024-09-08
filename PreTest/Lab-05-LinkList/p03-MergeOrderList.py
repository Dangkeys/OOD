"""

จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList จะมีแต่ Class Node ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้
createList() สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist
printList() สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว
mergeOrderList() สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว
****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****
****ห้ามสร้าง Class LinkList****

Enter 2 Lists : 1,3,5,7,10,20,22 4,6,7,8,15
LL1 : 1 3 5 7 10 20 22 
LL2 : 4 6 7 8 15 
Merge Result : 1 3 4 5 6 7 7 8 10 15 20 22 

Enter 2 Lists : 1,4,5,5,6,7 2,3,6,9,10
LL1 : 1 4 5 5 6 7 
LL2 : 2 3 6 9 10 
Merge Result : 1 2 3 4 5 5 6 6 7 9 10 

Enter 2 Lists : 2,2,2,10 1,1,1,1,5,5,5,6,7,8
LL1 : 2 2 2 10 
LL2 : 1 1 1 1 5 5 5 6 7 8 
Merge Result : 1 1 1 1 2 2 2 5 5 5 6 7 8 10 

"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    if len(l) == 0: return None
    head = Node(int(l[0]))
    p = head
    for i in range(1, len(l)):
        p.next = Node(int(l[i]))
        p = p.next
    return head

def printList(H):
    if H is None: return None
    lst = []
    p = H
    while p is not None:
        lst.append(str(p.data))  # Convert data to string before joining
        p = p.next
    print(' '.join(lst))

def mergeOrderedLists(p, q):
    if p is None: return q
    if q is None: return p
    if p.data < q.data:
        head = p
        p = p.next
    else:
        head = q
        q = q.next
    play = head
    while p is not None and q is not None:
        if p.data <= q.data:
            play.next = p
            p = p.next
        else:
            play.next = q
            q = q.next
        play = play.next
    if p is not None:
        play.next = p
    if q is not None:
        play.next = q
    return head

#################### FIX command ####################   
# input only a number save in L1,L2
input_lst = input("Enter 2 Lists : ").strip().split(" ")
L1 = input_lst[0].split(",")
L2 = input_lst[1].split(",")
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ', end='')
printList(LL1)
print('LL2 : ', end='')
printList(LL2)
m = mergeOrderedLists(LL1, LL2)
print('Merge Result : ', end='')
printList(m)

# This is Caesar cipher
# Enter Input : DATASTRUCTURE,30
# Encoded Message: HFZHACBFOGIGU
# Decoded Message: DATASTRUCTURE

# Enter Input : I Love KMITL,3
# Encoded Message: L Qucm UXUGZ
# Decoded Message: I Love KMITL