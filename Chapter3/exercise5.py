# หลังจากกฤษฎาเดินหลงป่ามาได้สักพักก็ได้ไปเจอเห็ดสีสันสวยงามจึงได้หยิบขึ้นมากิน  หลังจากกินเข้าไปทำให้กฤษฎามีอาการแปลกๆเกิดขึ้น  
# เนื่องจากเห็ดที่กินเข้าไปเป็นเห็ดพิษ  แต่กฤษฎาก็ยังคอยนับความสูงต้นไม้ไปเรื่อยๆเหมือนเดิม  
# ผลข้างเคียงจากเห็ดพิษก็ได้ส่งผลกระทบต่อการนับต้นไม้ของกฤษฎาเนื่องจากอาการหลอนประสาท 
# ทำให้ต้นไม้ที่มีความสูงเป็นเลขคี่มีการเพิ่มความสูงมา 2 เมตร และต้นไม้เลขคู่ลดความสูงไป  1 เมตร ความสูงที่น้อยที่สุดคือ 1 เมตร

class Stack:
    def __init__(self) -> None:
        self.items = []
        self.s_index = 0

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
    def S(self):
        self.items = [item + 2 if item % 2 == 1 else item -1 for item in self.items]

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
        elif action == 'S':
            stack.S()

    return '\n'.join(result)

user_input = input('Enter Input : ')
print(process_commands(user_input))
