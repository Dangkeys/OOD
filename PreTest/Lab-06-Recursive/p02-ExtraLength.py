"""

ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)
****ห้ามใช้คำสั่ง len, for, while, do while, split*****
หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

Enter Input : hello
h*e~l*l~o*
5

d*a~t*a~ *s~t*r~u*c~t*u~r*e~ *i~s* ~e*a~s*y~
22

Enter Input : *~*~*~
**~~**~~**~~
6

"""

def length(txt):
    if txt == '':
        return 0
    if txt[:1] != '':
        print(f"{txt[:1]}*", end="")
    if txt[1:2] != '':
        print(f"{txt[1:2]}~", end="")
        return 2 + length(txt[2:])
    return 1 + length(txt[1:])
        
string = input("Enter Input : ")
str_num = length(string)
print(f"\n{str_num}")