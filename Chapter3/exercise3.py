# หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   
# Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  "ผิดทั้งหมด!" 
# กฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน 
# โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 
# ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

# โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงจำนวนและลำดับของสีที่เหลือจากขวาไปซ้าย



class Stack:

    def __init__(self):
        self.items = []
        self.combo = 0
    def __str__(self) -> str:
        str_combo = f'\nCombo : {self.combo} ! ! !' if self.combo > 1 else ''
        str_items = ''.join([i for i in self.items])[::-1]  if not self.isEmpty() else 'Empty'
        return str_items + str_combo
    def push(self, value):
        return self.items.append(value)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items ==[]

    def peek(self, index):
        return self.items[index]
    def add_combo(self):
        self.combo += 1
    def delete(self, number):
        self.items = [num for num in self.items if num != number]
inp = input('Enter Input : ').split()

S = Stack()

### Enter Your Code Here ###




### Enter Your Code Here ###
for index, value in enumerate(inp):
    if S.isEmpty():
        S.items.append(value)
    else:
        if S.size() >= 2 and  value == S.peek(-1) and value == S.peek(-2) :
            S.delete(value)
            S.add_combo()
        else:
            S.items.append(value)
            

print(S.size())
print(S)