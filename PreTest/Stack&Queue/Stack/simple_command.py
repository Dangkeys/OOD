class Stack:
    def __init__(self) -> None:
        self.items = []
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() == 0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return -1
        return self.items.pop()
    def __str__(self) -> str:
        return str(self.items)
    def peek(self):
        return self.items[-1]
    
    def D(self, number):
        if self.is_empty():
            return -1
        self.items = [item for item in self.items if item != number]
        return self.items
        
    def LD(self, number):
        if self.is_empty():
            return -1
        self.items = [item for item in self.items if item < number]
        return self.items
    
    def MD(self, number):
        if self.is_empty():
            return -1
        self.items = [item for item in self.items if item > number]
        return self.items
    
    def run(self, user_input:str):
        command_list = user_input.split(',')
        for command in command_list:
            parts = command.strip().split()
            action = parts[0]
            if action == 'P':
                print(self.pop())
            elif action == 'A':
                print(self.push(parts[1]))
            # elif action == 'D':
            #     print(self.)
        
    
user_input = input('Enter Input : ')
s = Stack()
s.run(user_input)
