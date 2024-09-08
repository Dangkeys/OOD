"""

เขียนโปรแกรมที่แสดงผลดังตัวอย่าง
****ห้ามใช้คำสั่ง for, while, do while*****
หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

Enter Input : 3
__#
_##
###

Enter Input : 7
______#
_____##
____###
___####
__#####
_######
#######

Enter Input : -8
########
_#######
__######
___#####
____####
_____###
______##
_______#

Enter Input : 2
_#
##

Enter Input : 0
Not Draw!

"""

def staircase(main_n, sub_n):
    if main_n == 0: 
        return "Not Draw!"
    if main_n > 0:
        if main_n == 1:
            return "_" * (main_n - 1) + "#" * (sub_n + 1) + "\n"
        return "_" * (main_n - 1) + "#" * (sub_n + 1) + "\n" + staircase(main_n - 1, sub_n + 1)
    if main_n < 0:
        if main_n == -1:
            return "_" * abs(sub_n) + "#" * abs(main_n) + "\n"
        return "_" * abs(sub_n) + "#" * abs(main_n) + "\n" + staircase(main_n + 1, sub_n - 1)

number = int(input("Enter Input : "))
result = staircase(number, 0)
print(result)
