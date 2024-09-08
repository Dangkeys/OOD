"""  

****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่

Enter Input : abba
'abba' is palindrome

Enter Input : abgba
'abgba' is palindrome

Enter Input : abcdefkgfedfe
'abcdefkgfedfe' is not palindrome

"""

def palindrome(sent):
    if len(sent) < 2:
        return True
    elif sent[0] != sent[-1]:
        return False
    # print(sent[1:-1])
    return  palindrome(sent[1:-1])

sent = input("Enter Input : ")
if palindrome(sent):
    print(f"'{sent}' is palindrome")
else:
    print(f"'{sent}' is not palindrome")