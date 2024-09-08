""" 

****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

หา Factorial ของ input ที่รับมา โดยใช้ Recursive

Enter Number : 0
0! = 1

Enter Number : 1
1! = 1

Enter Number : 5
5! = 120

"""

def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return fac(n-1) * n

num = int(input("Enter Number : "))
print(f"{num}! = {fac(num)}")



