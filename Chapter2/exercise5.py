# จงสร้าง Class funString ที่จะรับพารามิเตอร์เป็น String และเลขคำสั่งโดยมีฟังก์ชันดังต่อไปนี้

# 1. หาความยาวของ String

# 2. สลับพิมพ์เล็กพิมพ์ใหญ่ใน String (ห้ามใช้คำสั่ง upper และ lower)

# 3. Reverse String (ห้ามใช้คำสั่ง reversed)

# 4. ลบตัวอักษรที่ปรากฏมาก่อนใน String


class funString():

    def __init__(self,string = ""):
        self.string = string
        ### Enter Your Code Here ###

    def __str__(self):
        return self.string
        ### Enter Your Code Here ###

    def size(self) :
        return len(self.string)
        ### Enter Your Code Here ###

    def changeSize(self):
        return ''.join([chr(ord(x) - 32) if x.islower() else chr(ord(x) + 32)  for x in self.string])
        ### Enter Your Code Here ###

    def reverse(self):
        return self.string[::-1]
        ### Enter Your Code Here ###

    def deleteSame(self):
        return ''.join(list(dict.fromkeys(self.string)))



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())