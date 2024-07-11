class ManageStack:
    def __init__(self, items=None) -> None:
        self.items = items if items else []

    def size(self):
        return len(self.items)

    def A(self, number):
        self.items.append(int(number))
        return f'Add = {number}'

    def P(self):
        return f'Pop = {self.items.pop()}' if not self.isEmpty() else '-1'

    def D(self, number):
        if self.isEmpty():
            return '-1'
        number = int(number)
        removed_items = [str(char) for char in sorted([int(i) for i in self.items if i == number])]
        self.items = [i for i in self.items if i != number]
        return removed_items
        
    def LD(self, number):
        if self.isEmpty():
            return '-1'
        number = int(number)
        removed_items = [i for i in self.items if i < number]
        self.items = [i for i in self.items if i >= number]
        return removed_items

    def MD(self, number):
        if self.isEmpty():
            return '-1'
        number = int(number)
        removed_items = [i for i in self.items if i > number]
        self.items = [i for i in self.items if i <= number]
        return removed_items

    def isEmpty(self):
        return len(self.items) == 0

    def __str__(self) -> str:
        return str(self.items) if not self.isEmpty() else '[]'

def process_commands(commands):
    output = []
    stack = ManageStack()
    command_list = commands.split(',')

    for command in command_list:
        parts = command.strip().split()
        action = parts[0]

        if action == 'A':
            result = stack.A(parts[1])
            output.append(result)
        elif action == 'P':
            result = stack.P()
            output.append(result)
        elif action == 'D':
            result = stack.D(parts[1])
            if result == '-1':
                output.append(result)
            elif result:
                for item in result:
                    output.append(f'Delete = {item}')
        elif action == 'MD':
            result = stack.MD(parts[1])
            if result == '-1':
                output.append(result)
            elif result:
                for item in result:
                    output.append(f'Delete = {item} Because {item} is more than {parts[1]}')
        elif action == 'LD':
            result = stack.LD(parts[1])
            if result == '-1':
                output.append(result)
            elif result:
                for item in result:
                    output.append(f'Delete = {item} Because {item} is less than {parts[1]}')

    output.append(f'Value in Stack = {stack}')
    return '\n'.join(output)

user_input = input('Enter Input : ')
print(process_commands(user_input))
