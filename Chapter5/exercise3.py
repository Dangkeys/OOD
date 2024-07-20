# จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList จะมีแต่ Class Node ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้

# createList() สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist

# printList() สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว

# mergeOrderList() สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว

# ****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****

# ****ห้ามสร้าง Class LinkList****


class node:
    def __init__(self,data,next = None ):
        ### Code Here ###
        pass
    def __str__(self):
        ### Code Here ###
        pass

def createList(l=[]):
    ### Code Here ###
    pass
def printList(H):
    ### Code Here ###
    pass
def mergeOrderesList(p,q):
    ### Code Here ###
    pass
#################### FIX comand ####################   
# input only a number save in L1,L2
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)