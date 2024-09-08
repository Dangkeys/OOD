"""

Have fun with encoding

เมื่อไม่นานมานี้พี่เป๋าเป่า พึ่งไปดูคลิปของ 9ARM มา เกี่ยวกับเครื่องถอดรหัส Enigma มาแล้วก็คิดว่า Encoding ก็หน้าสนใจดี ก็เลยจะให้โจทย์เป็นเขียน Encode แบบเครื่อง Enigmaโดยใช้ Recursion แต่พอมานั่งดูแล้วเดี๋ยวโจทย์มันจะโหดร้ายเกินไปและอธิบายยาก พี่เป๋าเป่าก็เลยตัดหลายๆอย่างออกไปจนกลายเป็น Caesar cipher ที่ใช้ Recursive ง่ายๆ โดยโจทย์มีการทำงานดังนี้
ให้น้องๆ รับ input เข้ามาโดยแบ่งเป็น 2 ส่วน ส่วนแรกคือคำที่เข้ารหัส และส่วนที่ 2 คือ จำนวนที่ต้องขยับ
***ตัวที่ใช้ Caesar cipher มีแค่ A-Z , a-z เท่านั้นตัวอื่นไม่ต้องเข้ารหัส และตัวอักษรที่ Encode ออกมาต้องไม่ใช่ตัวอักษรที่ใส่เข้าไปโดยให้ใส่เป็นตัวที่อยู่ลำดับถัดไปแทน***

อธิบายการทำงาน
Enter Input : aaaaaaaa,20
Encoded Message: uvwxyzbc
Decoded Message: aaaaaaaa

โดยในการ Encode 
ตัวแรก a -> u ขยับไป 20 ตัวอักษร
ตัวที่ 2 a -> v ขยับไป 20+1 ตัวอักษร
ไป เรื่อยเรื่อยถึงตัวที่ n จะขยับ (20 + (n-1))%26 ตัวอักษร

ถ้า Encode แล้วได้ตัวเอง เช่น a->a เพราะขยับ 26 ตัวให้ทำการข้ามตัวนั้นไปเลยเป็น a->b
แล้ว ให้ Decode กลับมา
โดยใช้หลักการคล้ายๆกัน
แถมเผื่อมีคนไม่ชอบ copy format

This is Caesar cipher
Enter Input : cat,5
Encoded Message: hga
Decoded Message: cat

This is Caesar cipher
Enter Input : DATASTRUCTURE,30
Encoded Message: HFZHACBFOGIGU
Decoded Message: DATASTRUCTURE

This is Caesar cipher
Enter Input : I Love KMITL,3
Encoded Message: L Qucm UXUGZ
Decoded Message: I Love KMITL

"""

def encode_char(char, rotor_position):
    if 'a' <= char <= 'z':
        encode_char = chr(((ord(char) - ord('a') + rotor_position) % 26) + ord('a'))
    elif 'A' <= char <= 'Z':
        encode_char = chr(((ord(char) - ord('A') + rotor_position) % 26) + ord('A'))
    else:
        encode_char = char
    if encode_char == char and char.isalpha():
        rotor_position += 1
        encode_char = chr(((ord(char) - ord(encode_char) + rotor_position) % 26) + ord(encode_char))
    rotor_position += 1
    return encode_char, rotor_position

def decode_char(char, rotor_position):
    if 'a' <= char <= 'z':
        decode_char = chr(((ord(char) - ord('a') - rotor_position) % 26) + ord('a'))
    elif 'A' <= char <= 'Z':
        decode_char = chr(((ord(char) - ord('A') - rotor_position) % 26) + ord('A'))
    else:
        decode_char = char
    if decode_char == char and char.isalpha():
        rotor_position += 1
        decode_char = chr(((ord(char) - ord(decode_char) + rotor_position) % 26) + ord(decode_char) - 2)
    rotor_position += 1
    return decode_char, rotor_position

def encode_message(message, rotor_position):
    if len(message) == 0:
        return ""
    else:
        char = message[0]
        encoded_char, rotor_position = encode_char(char, rotor_position)
        return encoded_char + encode_message(message[1:], rotor_position)

def decode_message(encoded_message, rotor_position):
    if len(encoded_message) == 0:
        return ""
    else:
        char = encoded_message[0]
        decoded_char, rotor_position = decode_char(char, rotor_position)
        return decoded_char + decode_message(encoded_message[1:], rotor_position)

print("This is Caesar cipher")
message, initial_rotor_position = input("Enter Input : ").split(',')
encoded = encode_message(message, int(initial_rotor_position))
print("Encoded Message:", encoded)
decoded = decode_message(encoded, int(initial_rotor_position))
print("Decoded Message:", decoded)
