""" 
ให้รับ Input เป็น  Infix  และแสดงผลลัพธ์ออกมาเป็น  Postfix  
โดยจะมี Operator  5  แบบ  ได้แก่  +   -   *   /   ^

Enter Infix : a+b
Postfix : ab+

Enter Infix : a+b*c
Postfix : abc*+

Enter Infix : a*b+c
Postfix : ab*c+

Enter Infix : a+b*c-d
Postfix : abc*+d-

Enter Infix : a+b*c-(d/e+f)*g
Postfix : abc*+de/f+g*-

Enter Infix : A+(B*C-(D/E^F)*G)*H
Postfix : ABC*DEF^/G*-H*+

Enter Infix : K+L-M*N+(O^P)*W/U/V*T+Q
Postfix : KL+MN*-OP^W*U/V/T*+Q+

KL+MN*-OP^W*+U/VT*/Q+

KL+MN*-OP^W*U/V/T*+Q+
"""


class Stack:

    def __init__(self, items = None) -> None:
        self.items = items if items else []
    
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() == 0
    def __str__(self) -> str:
        return str(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return 'Empty'
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return 'Empty'
        return self.items[-1]

def infix_to_postfix(expression: str):
    precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
    output = []
    s = Stack()
    
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            s.push(char)
        elif char == ')':
            while not s.is_empty() and s.peek() != '(':
                output.append(s.pop())
            s.pop()
        else:
            while not s.is_empty() and s.peek() != '(' and precedence.get(char,0) <= precedence.get(s.peek(),0):
                output.append(s.pop())
            s.push(char)
    
    while not s.is_empty():
        output.append(s.pop())
    
    return ''.join(output)

user_input = input("Enter Infix: ")
postfix_expression = infix_to_postfix(user_input)
print("Postfix:", postfix_expression)
