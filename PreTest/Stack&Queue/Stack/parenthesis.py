class Stack:
    parenthesis_list = ['(', ')', '[', ']']
    matching_parenthesis = {'(': ')', '[': ']'}

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

    def run(self, user_input: str):
        for char in user_input:
            if char in self.parenthesis_list:
                if not self.is_empty() and self.peek() in self.matching_parenthesis and self.matching_parenthesis[self.peek()] == char:
                    self.pop()
                else:
                    self.push(char)
        print(self.items)
        print(self.size())
        print('Perfect ! ! !' if self.size() == 0 else '')

parenthesis = Stack()
user_input = input("Enter Input: ")
parenthesis.run(user_input)
