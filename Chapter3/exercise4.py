class Stack:
    def __init__(self) -> None:
        self.items = []

    def peek(self):
        return self.items[-1]

    def A(self, item):
        self.items.append(int(item))

    def B(self):
        if self.isEmpty():
            return 0
        
        visible_count = 0
        max_height = 0

        for height in reversed(self.items):
            if height > max_height:
                visible_count += 1
                max_height = height
        
        return visible_count

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

def process_commands(commands):
    result = []
    stack = Stack()
    command_list = commands.split(',')

    for command in command_list:
        parts = command.strip().split()
        action = parts[0]

        if action == 'A':
            stack.A(parts[1])
        elif action == 'B':
            result.append(str(stack.B()))

    return '\n'.join(result)

user_input = input('Enter Input : ')
print(process_commands(user_input))
