# จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList 
# จะมีแต่ Class Node ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้

# createList() สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist

# printList() สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว

# mergeOrderList() สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value 
# โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว

# ****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****

# ****ห้ามสร้าง Class LinkList****


class Node:
    def __init__(self,data,next = None ):
        ### Code Here ###
        self.data = data
        self.next = next
    def __str__(self):
        ### Code Here ###
        return self.data

def createList(l=[]):
    head = Node(l[0])
    current_node = head
    for value in l[1:]:
        current_node.next = Node(value)
        current_node = current_node.next
    return head

def printList(H):
    current_node = H
    while current_node:
        print(current_node.data, end=' ')
        current_node = current_node.next
    print()

def mergeOrderesList(p,q):
    if not p:
        return q
    if not q:
        return p
    if p.data <= q.data:
        head = p
        p = p.next
    else:
        head = q
        q = q.next
    current_node = head
    while p and q:
        if p.data <= q.data:
            current_node.next = p
            p = p.next
        else:
            current_node.next = q
            q = q.next
        current_node = current_node.next
    if p:
        current_node.next = p
    elif q:
        current_node.next = q
    return head
#################### FIX comand ####################   
# input only a number save in L1,L2
L1, L2 = [list(map(int, x.split(','))) for x in input('Enter 2 Lists : ').split()]

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)
