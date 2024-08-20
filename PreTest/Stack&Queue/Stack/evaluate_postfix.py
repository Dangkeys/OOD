'''
 * กลุ่มที่  : 24010116
 * 66010289 ตฤณ ขุนเณร
 * chapter : 3	item : 3	ครั้งที่ : 0002
 * Assigned : Thursday 11th of July 2024 09:38:47 AM --> Submission : Thursday 11th of July 2024 10:24:38 AM	
 * Elapsed time : 45 minutes.
 * filename : 3.py
 Chapter : 3 - item : 3 - Postfix Calculator
 ส่งมาแล้ว 2 ครั้ง
จงเขียนโปรแกรมโดยใช้ Stack เพื่อคำนวณหา ค่าของนิพจน์แบบ postfix 

โดยให้แสดงผลลัพธ์ตามตัวอย่าง



class Stack():

    def __init__(self, ls = None):

    def push(self,i):

    def pop(self):

    def isEmpty(self):

    def size(self):

def postFixeval(st):

    s = Stack()

    ### Enter Your Code Here ###

    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))
Testcase student: #1/5 1
 ***Postfix expression calcuation***
Enter Postfix expression : 6 5 2 3 + 8 * - 3 + *
Answer :  -192.00

Testcase student: #2/5 2
 ***Postfix expression calcuation***
Enter Postfix expression : 4 22 * 89 / 98 * 21 - 32 2 / 4 * 10 / 23 * + 23 -48 * -
Answer :  1327.10

Testcase student: #3/5 3
 ***Postfix expression calcuation***
Enter Postfix expression : 5 8 * 5 6 * 6 6 4 * - 5 6 * 6 / + - -
Answer :  -3.00

Testcase student: #4/5 4
 ***Postfix expression calcuation***
Enter Postfix expression : 3 8 2 / 6 * 5 6 - + 6 6 -5 5 * 2 - - + + +
Answer :  65.00


'''
class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = len(self.items)

    def push(self, i):
        self.items.append(i)
        self.size += 1

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[ -1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items) 
    def postFixeval(st):
        s = Stack()
        for i in st:
            print(i)
            if i not in "+-*/":
                s.push(int(i))
            else:
                right = s.pop()
                left = s.pop()
                if i == '+': s.push(left+right)
                if i == '-': s.push(left-right)
                if i == '*': s.push(left*right)
                if i == '/': s.push(left/right)
        return s.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(Stack.postFixeval(token)))