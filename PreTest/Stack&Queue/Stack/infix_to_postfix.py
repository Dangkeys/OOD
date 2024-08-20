class Stack:

    def __init__(self, items=None) -> None:
        if items is None:
            self.items = []
        else:
            self.items = items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    output = []

    for char in expression:
        if char.isalnum():  # Check if the character is an operand
            output.append(char)
        elif char == '(':  # If the character is '(', push it to stack
            stack.push(char)
        elif char == ')':  # If the character is ')', pop until '(' is found
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '(' from the stack
        else:  # The character is an operator
            while (not stack.is_empty() and stack.peek() != '(' and precedence.get(char, 0) <= precedence.get(stack.peek(), 0)):
                output.append(stack.pop())
            stack.push(char)

    # Pop all the operators from the stack
    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)

user_input = input("Enter Infix: ")
postfix_expression = infix_to_postfix(user_input)
print("Postfix:", postfix_expression)
