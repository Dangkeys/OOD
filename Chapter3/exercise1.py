# ให้น้องๆเขียนโปรแกรมรับ input เป็นวงเล็บ โดยมีรูปแบบดังนี้  วงเล็บเปิด :  (  กับ  [    วงเล็บปิด :  )  กับ  ]   
# โดยให้หาว่าถ้าหากนำวงเล็บมาจับคู่กัน จะครบทุกคู่หรือไม่  
# โดยให้แสดงผลลัพธ์ออกมาเป็นจำนวนวงเล็บที่จะต้องเติมหากวงเล็บมีไม่ครบคู่   แต่ถ้าหากครบคู่ให้แสดงคำว่า  Perfect  ออกมาด้วย

user_input  = input('Enter Input : ')
matching_parenthesis = {'(':')','[':']',}
class Stack:
    total = 0
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def __str__(self) -> str:
        return ''.join([c for c in self.items])
stack = Stack()
for char in user_input:
    
    if not stack.isEmpty():
        if stack.peek() in matching_parenthesis and char == matching_parenthesis[stack.peek()]:
            stack.pop()
        else:
            stack.push(char)
    else:
        stack.push(char)
print('0\nPerfect ! ! !' if stack.isEmpty() else stack.size())