class Stack:
    def __init__(self, ls=None):
        if ls is None:
            self.items = []
        else:
            self.items = ls

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def postFixeval(st):
    s = Stack()

    for token in st:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  # Check if the token is an operand
            s.push(int(token))
        else:
            # The token is an operator, pop the top two elements
            b = s.pop()
            a = s.pop()
            if token == '+':
                s.push(a + b)
            elif token == '-':
                s.push(a - b)
            elif token == '*':
                s.push(a * b)
            elif token == '/':
                s.push(a / b)
    
    return s.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))
