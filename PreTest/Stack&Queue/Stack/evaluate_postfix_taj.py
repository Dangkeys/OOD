# # Testcase student: #1/5 1
# #  ***Postfix expression calcuation***
# # Enter Postfix expression : 6 5 2 3 + 8 * - 3 + *
# # Answer :  -192.00

# # Testcase student: #2/5 2
# #  ***Postfix expression calcuation***
# # Enter Postfix expression : 4 22 * 89 / 98 * 21 - 32 2 / 4 * 10 / 23 * + 23 -48 * -
# # Answer :  1327.10

# # Testcase student: #3/5 3
# #  ***Postfix expression calcuation***
# # Enter Postfix expression : 5 8 * 5 6 * 6 6 4 * - 5 6 * 6 / + - -
# # Answer :  -3.00

# # Testcase student: #4/5 4
# #  ***Postfix expression calcuation***
# # Enter Postfix expression : 3 8 2 / 6 * 5 6 - + 6 6 -5 5 * 2 - - + + +
# # Answer :  65.00




class Stack:
    def __init__(self,items = None) -> None:
        if items == None:
            self.items = []
        else:
            self.items = items
    def __str__(self) -> str:
        return str(self.items)
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() == 0
    def peek(self):
        return self.items[-1]
    def pop(self):
        if self.is_empty():
            return 
        return self.items.pop()
    def push(self,item):
        self.items.append(item)
        
def postFixeval(st: str):
    
    s = Stack()

    ### Enter Your Code Here ###
    for token in st:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            s.push(int(token))
            continue
        right = s.pop()
        left = s.pop()
        if token == '+':
            s.push(left + right)
        elif token == '-':
            s.push(left - right)
        elif token == '*':
            s.push(left * right)
        elif token == '/':
            s.push(left / right)
            
        
    return s.pop()

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))